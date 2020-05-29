Title: Introducing React to the legacy application
Slug: introducting-react-to-legacy-application
Date: 2020-05-18 12:45:00
Tags: react, microfrontend
Category: programming
Authors: Aleksander Chrabąszcz
Summary: Integrating React (CRA) with a legacy server-side rendered website
Status: draft

Recently I was doing some stuff in order to introduce more modern frontend for a (relatively big) website that is rendered on the server side - a browser-based role-playing game called [Cantr](https://cantr.net). The application is pretty big when compared to amount of my free time, so it's impossible to just rewrite everything in one go.

I'm going to explain how I've set up the following things:

 - initial CRA Setup
 - how to plug-in react root components (rendered using ReactDOM.render) into the existing page structure
 - how I've setup a convenient development environment
 - how to add Bootstrap styles to React without affecting the rest of the page
 - how I've handled communication between React components and existing jQuery code

# How it was

The application uses a very old setup: PHP server which renders (mostly) static HTML using Smarty. Some dynamic things are handled using a decent amount of jQuery scripts for simple AJAX requests and DOM manipulation. The code has many problems. It doesn't use any CSS framework or even a standard, so it's painful to add new features. One good thing is that CSS (which were written by hand every time something new was added) is rendered using SCSS. Everything runs on Apache and MySQL without help of any framework, so it's a role model of being legacy. Oh, and I forgot to mention it's still on PHP 5 because not all incompatibilities with PHP 7 were fixed yet. And the available API is minimal.

Another challenge was to be able to style new React components independently from the rest of the site, because even some general reset/normalize stylesheets will affect the old frontend.

I hope not many of you will ever have to maintain a similar technology stack and this decision to add React (with a potential) looks karkołomna, but I see no other way to be able to provide features in the short-term. My plan is to make sure all the components will be isolated from unclean DOM-integration through an intermediate layer of wrapper components, so everything except them will be able to be moved to a proper SPA in the future.

(diagram with site,  react root component, pure react components)

I've started with creating a typescript project:

```yarn create ... typescript```

How to use devserver.

CORS

react-rewired

How to know when to request from localhost:3000?

Serve from docker for consistency

```
react_1        | ℹ ｢wds｣: Project is running at http://172.21.0.5/
react_1        | ℹ ｢wds｣: webpack output is served from 
react_1        | ℹ ｢wds｣: Content not from webpack is served from /app/cantr-frontend/public
react_1        | ℹ ｢wds｣: 404s will fallback to /
react_1        | Starting the development server...
react_1        | 
react_1        | Done in 2.55s.
docker_react_1 exited with code 0
```

WTF? When running manually after doing `docker exec -ti docker_react_1 bash` everything went fine. After some time searching I've learned that it's because after some update CRA requires specifying a environment variable `CI=true` in order to not exit quietly when no terminal is attached. How sweet.

```yml
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

Works!

Passing data into components? `data-*`

Listening to events from jQuery

