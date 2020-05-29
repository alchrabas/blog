Title: Introducing React into the legacy application
Slug: introducting-react-into-legacy-application
Date: 2020-05-18 12:45:00
Tags: react, microfrontend
Category: programming
Authors: Aleksander Chrabąszcz
Summary: Integrating React (CRA) with a legacy server-side rendered website

Recently I was doing some work in order to introduce a more modern **React** frontend for a (relatively big) website that is rendered on the server side - a browser-based role-playing game called [Cantr](https://cantr.net). The application is pretty big when compared to the amount of my free time, so it's impossible to just rewrite everything in one go. That's why I looked for a solution that makes gradual improvement possible.

I'm going to present how I've set up the following things:

1. Initial **Create React App (CRA)** setup and how to plug-in react root components into the existing page structure
2. How I've setup a convenient development environment
3. How to add **Bootstrap** styles to React without affecting the rest of the page
4. How to handle communication between React components and existing jQuery code

# How it was

The application uses a very old setup: PHP server which renders (mostly) static HTML using [Smarty](https://www.smarty.net/). Some dynamic things are handled using a decent amount of jQuery scripts for simple AJAX requests and DOM manipulation. The code has many problems. It doesn't use any CSS framework or even a standard, so it's painful to add new features. One good thing is that CSS (which was modified every time something new was added) is processed using SCSS. Everything runs on Apache and MySQL without help of any framework, so it's a role model of being legacy. Oh, and I forgot to mention it's still on PHP 5 because not all incompatibilities with PHP 7 were fixed yet. And the available API is minimal.

Another challenge was to be able to style new React components independently from the rest of the site, because even some general reset/normalize stylesheets would affect the old frontend.

I hope not many of you will ever have to maintain a similar technology stack and this decision to add React looks hazardous, but I see no other way to be able to provide new features in the short-term. My plan is to make sure all the new components are isolated from unclean DOM-integration through an intermediate layer of wrapper components, so everything except the wrappers will be moved to a proper SPA in the future.

In this text I'll call every independent and isolated React component **microfrontend**, even though it's an exaggeration. They aren't built or deployed separately and, because of technical limitations, there is some coupling between them and the parent page. But this name makes it sound more cool.

![ReactMicrofrontend with pure React components is docked between standard HTML and jQuery based components](/images/attaching-react-to-legacy-application/microfrontend-diagram.png)

# 1. Initial Create React App (CRA) setup 

I've started with creating a typescript project:

```text
yarn create react-app cantr-frontend --template typescript
```

Then I've created the first simple microfrontend called `PlayerTopBarMicrofrontend` and made it render on `index.html` page.

To do it, I've created a div in `index.html`'s body: `<div id="playerTopBar" />` and then added the following code in `index.tsx` to render React component in the div:

```jsx
ReactDOM.render(
  <React.StrictMode>
    <PlayerTopBarMicrofrontend />
  </React.StrictMode>,
  document.getElementById("playerTopBar")
);
```

The similar code will be needed to add another microfrontends in the future.

The directory structure of all the projects looks like that:

```
app/
  cantr-frontend/        <- React application
    src/
  www/                   <- webroot of the legacy application
  docker/
    docker-compose.yaml  <- docker-compose config for running the legacy app in dev mode
```

After ensuring it works, I've started the work on integrating it with the Cantr's existing frontend.

## Adding React production build as part of old frontend

The first goal is to be able to run normal `yarn build` to create static files and then request them from the main page's `index.php`. In the normal setup, these files are required in React's `index.html` and served by a webserver like nginx.

`yarn build` creates the following directory structure in directory `build/`:

```text
build
├── index.html
├── manifest.json
└── static
    ├── css
    │   └── main.1d613f07.chunk.css
    └── js
        ├── 2.0eb6c152.chunk.js
        ├── 2.0eb6c152.chunk.js.LICENSE.txt
        ├── main.d78e528d.chunk.js
        └── runtime-main.a0f90d88.js
```

(some files were omitted for brevity)

Multiple JS and CSS files are because of Create React App's chunking abilities. In a normal Single Page App JS and CSS files are downloaded from the server only when they are needed. Unfortunately I see no way to use this mechanism when adding microfrontends to the legacy application.

To make these files accessible for main application, I've added a command to `package.json` which, after running `build`, copies the static JS and CSS files under main application's webroot (`../www/`):

```text
"cantr-build":"yarn build && rm -rf ../www/react/* && cp -r build/static/* ../www/react/",
```

Then, when the page is requested, I check the content of these directories in PHP code and import them:

`index.php`:
```php
$smartyTeplate->assign("reactJs", array_filter(scandir("react/js"), function($file) {
  return StringUtil::endsWith($file, ".js");
}));
```

`index.tpl` (smarty template):
```
{foreach $reactJs as $js}
<script type="text/javascript" src="/react/js/{$js}"></script>
{/foreach}
```

(exactly the same was done for CSS files)

The last part was to add a div with id `playerTopBar` somewhere in Smarty template and everything started working.

# 2. Using React's devserver as part of legacy application's development

The first version of serving production code was working, but at least as important is to have good development experience - to be able to modify React code and immediately see the changes as part of the main Smarty-based application.

React's devserver is a simple Express-based server which awaits for any changes in source files, compiles them in the background and refreshes the SPA in the browser. I wanted to be able to see the changes done in the React Microfrontend after refreshing the page of the main PHP application that contains them.

I had to solve a few problems to make it work this way. First of all, React devserver is served on address localhost:3000 while the PHP application served by dockerized Apache is accessible at localhost:8083. An obvious issue arises...

## CORS

Because of a different port, accessing JS files is considered a cross-origin request. After investigating a few solutions (proxying, disabling CORS check in the browser for development) I've deicded that the simplest solution is to make files served by React's devserver accessible from any origin. Unfortunately, CRA doesn't give an easy config option to just disable CORS check, and devserver's code cannot be manipulated directly, because it's hidden by CRA. I had to use [react-app-rewired](https://github.com/timarney/react-app-rewired) to overwrite devserver's configuration and set header `Access-Control-Allow-Origin: *`.

## Disable chunking for development

Because of the chunking mechanism it's hard to predict what file names should be imported by the main application's devserver. It was easy for production, because the generated files were accessible to the server, but the ones served by React devserver were not existing physically.

I've decided that the simplest solution is to make the file names easy to guess by disabling chunking in dev mode. As a result, everything is stored and served as a single file, accessible from the path `http://localhost:3000/static/js/bundle.js` (it contains both JavaScript and CSS). The config change was also done using react-app-rewired.

The final version of react-app-rewired's `config-overrides.js`, that disables chunking and CORS for dev mode, looks like that:

```javascript

module.exports = {
  webpack: function(config, env) {
    if (env === "development") {
      config.optimization.splitChunks = {
        cacheGroups: {
          default: false,
        },
      };
      config.optimization.runtimeChunk = false;
    }
    return config;
  },
  devServer: function(configFunction) {
    return function(proxy, allowedHost) {
      const config = configFunction(proxy, allowedHost);
      config.headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
      };
      return config;
    };
  },
};
```

## How to know when to serve JS from devserver?

Now it's possible to load the React components from the devserver, but one problem still exists: when to actually do it?

My first idea was to connect to localhost:3000, see if there is any response and, if not, then load the static files from last production build. After some attempts I've decided it's not a good idea, because:

1. It's complicated
2. It's error-prone
3. Even on production the client's browser would make a request to devserver before requesting production files, which would mean slower loading

My second thought was to configure a reverse proxy, but it was also complicated.

So I went with the simplest idea. In some other webserver I'd probably make it controllable by an environment variable. It's not possible in Cantr, but there's almost equally good solution of storing this value in JSON configuration file. Configuration value "devserverMode" is injected into Smarty template which allows to write a simple condition like that:

```php
{if $devserverMode}
<script type="text/javascript" src="http://localhost:3000/static/js/bundle.js"></script>
{else}
{foreach $reactJs as $js}
<script type="text/javascript" src="/react/js/{$js}"></script>
{/foreach}
{/if}
```

## Serve from docker for consistency

So far I was running `yarn start` directly on my host terminal, but, since all the other services (Apache, MySQL, SASS) of the legacy application are run using docker-compose, yarn should also be dockerized to make it easy for a new programmer to start working with the codebase.

Yarn is available in a standard `node` image, so I thought it will be super easy to do. Unfortunately, after running `yarn start` in docker for the first time, I've noticed the following error:

```php
react_1     | ℹ ｢wds｣: Project is running at http://172.21.0.5/
react_1     | ℹ ｢wds｣: webpack output is served from 
react_1     | ℹ ｢wds｣: Content not from webpack is served from /app/cantr-frontend/public
react_1     | ℹ ｢wds｣: 404s will fallback to /
react_1     | Starting the development server...
react_1     | 
react_1     | Done in 2.55s.
docker_react_1 exited with code 0
```

WTF? When running `yarn start` manually after doing `docker exec -ti docker_react_1 bash`, everything is working fine. I started to scratch my head and look for the cause of the hidden error.

After some time, I've learned it is because (since some minor update) CRA requires specifying an environment variable `CI=true` in order to not exit quietly when no terminal is attached. How sweet. The following service in docker-compose works like a charm:

```yaml
        react:
                image: node:12.16.2-stretch
                environment:
                        - NODE_ENV=development
                        - CHOKIDAR_USEPOLLING=true
                        - CI=true
                volumes:
                        -  ..:/app/
                ports:
                        - "3000:3000"
                        - "35729:35729"
                command: ["bash", "-c", "cd /app/cantr-frontend/ && yarn start"]
```

`CHOKIDAR_USEPOLLING=true` and mapping of port 35729 were suggested [somewhere on GitHub](https://github.com/facebook/create-react-app/issues/1049#issuecomment-261731734) to make hot code replacement work.

# 3. Bootstrap styles

It was the most important issue since the beginning. It had to be possible to add some UI library to React components without affecting the styles of the existing legacy application. If not possible, it would beat the purpose of introducing React, because I would still need to write a lot of CSS boilerplate to style every new component and not be able to use some CSS reset/normalize.

These requirements made me think that Bootstrap (with global scoped CSS class names like "btn btn-primary", which are defined separately from React-Bootstrap) might not be a perfect fit.

It would be easier to use a library like [Material UI](https://material-ui.com/), which transforms styles for each component into a globally unique CSS class, which is then attached to a single DOM element, so there is a guarantee of no clashes. I would go that path, but I really don't like JSS and, since Material UI is a much heavier library in general, I've started to experiment with good old Bootstrap and [React-Bootstrap](https://github.com/react-bootstrap/react-bootstrap).

First of all, every microfrontend (top-level React component) needs to wrap all the other components in a div with a specific class, in my case `react-component`:

```tsx
const PlayerTopBarMicrofrontend = () => (
  <div className="react-component">
    <PlayerNavBar/>
  </div>
);
```

To make use of (global) Boostrap SCSS styles, I had to modify the tutorial from [React-Bootstrap's documentation](https://react-bootstrap.github.io/getting-started/introduction#sass) by wrapping all its contents into one parent class.

index.scss:
```scss
@import "~bootstrap/scss/bootstrap";
```

became

```scss
.react-component {
  @import "~bootstrap/scss/bootstrap";
}
```

Then, every React component rendered inside can use CSS modules with only minor changes. Here example of `NewCharacterButton` component:

```tsx
import React from "react";
import styles from "./NewCharacterButton.module.scss";
import Button from "react-bootstrap/Button";
import classNames from "classnames";

const NewCharacterButton = () => (
  <Button className={classNames("bg-transparent", styles.button)}>
    Click me
  </Button>
);
```

`bg-transparent` is a bootstrap CSS class, while `styles.button` contains my custom styles:

NewCharacterButton.module.scss:
```scss
@import "../../global";

:global(.react-component) {
  .button {
    border: none;
    background: none;
    color: #fff;
  }
}
```

The only change that is needed in every CSS module is to prefix all the style classes with ".react-component" (:global is used to take this class name literally, without CSS class hashing). After transforming the whole frontend into SPA it will be enough to remove this `:global` line.

# 4. Communication between React and the old code

It would be best to develop each microfrontend in isolation, making it responsible for communication with the API to the extent that is necessary to render the UI. But since there's almost no API and large part of data used by JQuery is baked into static pages rendered server-side, it might be necessary to reuse that data in the microfrontend. I've decided to organize components the following way:

1. almost all React components get the values to render from the props, are pure and testable
2. top-level components for each microfrontend can perform "unclean" operations like communication with anything outside of the microfrontend (getting data from the rest of the site, listening to DOM events)

## Passing data into components

The last time I have full control over clean data is when rendering Smarty templates on the server, so I've decided to pass the data through properties of HTML object.

somePage.tpl (smarty template):

```html
<div id="characterTopBar" data-inventory-weight="100" />
```

The Microfrontend component is not pure anyway, so it might be aware of the place in the DOM tree where it's located:
 
```tsx
const CharacterTopBarMicrofrontend = () => {
  const characterTopBar = document.getElementById("characterTopBar");
  const initialInventoryWeight = characterTopBar
      ? Number(characterTopBar.dataset.inventoryWeight as string)
      : 0;
  const [inventoryWeight, setInventoryWeight] = useState(initialInventoryWeight);
  return (
    <div className="react-component">
      <CharacterNavBar inventoryWeight={inventoryWeight}/>
    </div>
  );
}
```

CharacterNavBar and all child components are all pure.

It might be better to move this unclean code to `useEffect` but, assuming the outer HTML is rendered statically, it doesn't ever change, so it doesn't matter in this simple example.

## Listening to events from jQuery

I think a need for such communication should never happen, because, if needed, each microfrontend can fetch the current state of the application from the backend, without resorting to the data that is already in the browser. But, to confirm it's possible, I've created a PoC of a React hook that allows listening for jQuery (DOM) events. If ever used, this should be called only in top-level wrapper components.

```typescript
export const useDomEvent = (eventName: string, fn: ({ detail: any }) => void) => {
  useEffect(() => {
    document.body.addEventListener(eventName, fn);
    return () => document.body.removeEventListener(eventName, fn);
  }, [eventName, fn]);
};
```

The jQuery should then trigger custom events for `document.body` DOM node.

# Summary

I'm glad that, despite all the problems, I've managed to plug React into existing server-side-rendered application.
 
There are of course some shortcomings, for example React components are rendered from scratch every page load, but, assuming the state is stored server-side, it's good enough to make a step forward in gradual replacement of old interface.
