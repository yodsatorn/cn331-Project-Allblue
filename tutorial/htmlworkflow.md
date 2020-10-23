# Html work flow

This is a tutorial for basic html and our work flow for cn331-Project-Allblue

- [Must know html tag](#Must-know-html-tag)
- [html Construction Example](#html-Construction-Example)
- [Work flow](#Work-flow)

## Must know html tag

### block element

Block element always **starts on a new line and takes up the full width available** (stretches out to the left and right as far as it can).

[READ](https://www.w3schools.com/html/html_blocks.asp)

#### div

normally, we use `<div>` tag to divide each section and provide them with styled using CSS.

```html
<style>
.myDiv {
  border: 5px outset red;
  background-color: lightblue; 
  text-align: center;
}
</style>

<div class="myDiv">
  <h2>This is a heading in a div element</h2>
  <p>This is some text in a div element.</p>
</div>
```

#### h1 - h6

heading tag is used to defind heading.

`<h1>` defines the most important heading. `<h6>` defines the least important heading.

```html
<h1>This is heading 1</h1>
<h2>This is heading 2</h2>
<h3>This is heading 3</h3>
<h4>This is heading 4</h4>
<h5>This is heading 5</h5>
<h6>This is heading 6</h6>
```

#### p

p tag is used to defind paragraph. Browsers automatically add a single blank line before and after each `<p>` element.

```html
<p>This is some text in a paragraph.</p>
```

### in-line element

An inline element **does not start on a new line and it only takes up as much width as necessary**.

[READ](https://www.w3schools.com/html/html_blocks.asp)

#### strong

The `<strong>` tag is used to define text with strong importance. The content inside is typically displayed in bold.

```html
<strong>This text is important!</strong>
```

#### b

The `<b>` tag specifies bold text without any extra importance.

```html
<p>This is normal text <b>and this is bold text</b>.</p>
```

##### strong VS b

`<strong>` is used to indicate that this context is *important* unlike `<b>` that used to specify bold text *without any extra importance*.

There are many tags that looks identical but differences in context and usage.

#### a

The `<a>` tag defines a hyperlink, which is used to link from one page to another.

```html
<a href="https://github.com/6110613228/cn331-Project-Allblue">Github page</a>s
```

### html Construction Example

```html
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
  <head>
    <meta charset="UTF-8" />
    <title>My Website</title>
    <link rel="stylesheet" href="style/grid-demo2.css">
  </head>
  <body>
    <div class="container">
      <header class="site-header">
        <h1>My Website</h1>
        <p>This is the slogan of my website.</p>
        <nav class="site-nav">
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About us</a></li>
            <li><a href="#">Blog</a></li>
            <li><a href="#">Contact US</a></li>
          </ul>
        </nav>
      </header>
        <div class="line"></div>
        <main class="main-area">
          <article>
            <header>
              <h2>First Article</h2>
              <p>Posted on Aug, 2 2015</p>
            </header>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras facilisis et
                urna vel hendrerit. Curabitur ultrices eu arcu et gravida. Suspendisse at
                pharetra lorem, quis condimentum arcu. In hac habitasse platea dictumst.
              </p>
              <p>Category: Lorem ipsum</p>
            </article>
            <article>
              <header>
                <h2>Second Article</h2>
                <p>Posted on Aug, 1 2015</p>
              </header>
              <p>
                In ligula sapien, faucibus eget maximus quis, blandit ullamcorper augue.
                Etiam in rutrum quam. Praesent consectetur purus a nibh mattis egestas.
              </p>
              <footer>
                <p>Category: In lingu</p>
              </footer>
          </article>
        </main>

        <aside class="sidebar-area">
          <article>
            <header>
              <h2>Sidebar</h2>
            </header>
            <p>
              Sed id sodales felis, non consequat felis. Phasellus nibh ex, vehicula vel
              egestas eu, mattis et nunc. Sed nec justo diam. Proin tincidunt
              condimentum tellus, sed vulputate elit sagittis vel. Quisque bibendum dui
              id velit venenatis lacinia.
            </p>
          </article>
        </aside>
        <footer class="side-footer">
          <p class="footer">&copy;2015 My Website</p>
        </footer>
    </div>
  </body>
</html>

```

We normally seperate each main section with `<div>` and **given them a class to be able to control them with style sheet**.

link with css:

```html
<link rel="stylesheet" href="style/grid-demo2.css">
```

The option `rel="stylesheet"` is important it's indicate that this is a link to stylesheet.

Inside grid-demo.css

```css
html {
    background-color: rgb(115, 168, 115);
}

boby {
    font-family: Tahoma, sans-serif;
}

.container {
    display: grid;
    grid-template-columns: 2fr 1fr;
    grid-template-rows: auto auto auto;
    grid-template-areas: 
        "header header"
        "line line"
        "main sidebar"
        "footer footer";
    background-color: white;
    max-width: 945px;
    margin: auto;
}

.site-header {
    grid-area: header;
    grid-column: 1/3;
    grid-row: 1/2;
    padding-left: 40px;
    padding-right: 40px;
}

.main-area {
    grid-area: main;
    grid-column: 1/2;
    grid-row: 2/3;
    padding-left: 40px;
    padding-right: 20px;
}

.sidebar-area {
    grid-area: sidebar;
    grid-column: 2/3;
    grid-row: 2/3;
    padding-right: 40px;
} 

.side-footer {
    grid-area: footer;
    grid-column: 1/3;
    grid-row: 3/4;
    padding-left: 40px;
    padding-right: 40px;
}

h1 {
    margin-bottom: 0;
}

header h1 + p {
    margin-top: 0;
}

article header h2 {
    margin-bottom: 0;
}

article header p {
    margin-top: 0;
}

p.footer {
    border-top: 2px solid gray;
    padding-top: 10px;
    padding-bottom: 20px;
}

.site-nav ul {
    margin-top: 30px;
    margin-left: 0;
    padding: 0;
}

.site-nav ul li {
    list-style: none;
    float: left;
    margin-right: 5px;
}

.site-nav a {
    display: block;
    text-decoration: none;
    color: green;
    padding: 5px 20px;
    border: 2px solid dimgray;
    border-bottom: none;
}

.site-nav a:hover {
    background-color: lightgreen;
}

.line {
    grid-area: line;
    border-top: 3px solid gray;
    margin-left: 40px;
    margin-right: 40px;
}
```

h1 + p is call specificity oparator.

[READ ABOUT SPECIFICITY](https://www.w3schools.com/css/css_specificity.asp)

## Work flow

### Using layout-topnav.html

[layout-topnav.html](../index/templates/layout-topnav.html)

You can import layout-topnav.html to your html file by using Django's template tag.

> {% extends "layout-topnav.html" %}

extends **doesn't require {% endblock %}**

Inside layout-topnav.html include

1. Block title
2. Block head
3. Block link
4. Block body

Block title is for indicate your title's page.

Block head is for include something in html head.

Block link is for link css flie.

Block body is for include your html body.

For example.

**Yourhtml.html**
```html
{% extends "layout-topnav.html" %}
<!-- If you are using static in your own html don't forget to load static -->
{% load static %}
{% block title %} Homepage {% endblock%}
{% block link %} {% static "index/css/YOURCSSFILE.css" %} {% endblock %}
{% block head %}
  <!-- Your html head -->
  <!-- For example. -->
  <link rel="stylesheet" type="text/css" href="MORESTYLE.css">
{% endblock %}
{% block body %}

Your Body block.

{% endblock %}
```

### Seperating CSS file

### django template tags

[READ](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/)

1. [Block](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#block)
2. [extends](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#extends)
3. [url](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#url)
4. [include](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#include)
5. [static](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#static)
