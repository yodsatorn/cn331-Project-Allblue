# Html work flow

This is a tutorial for basic html and our work flow for cn331-Project-Allblue

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

## Work flow

### Using reserved django's block tag

### How to use django template tag

#### url

#### static
