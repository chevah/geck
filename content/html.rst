HTML, XML and other markups
###########################

:menu_order: 153
:slug: html

.. contents::


General
=======

* Unlike other files, indentation for XML/HTML is 2 spaces. 

* Don't use inline HTML style attributes. Only CSS classes.

* Use HTML5 doctype::

    <!doctype html>


CSS interaction
===============

* Make sure all elements that are used in JS have an ID.
  This helps with testing.

* Make sure all related elements have the same class.

* Make sure that a page will not contain the same ID more than once.


HTML tags usage
===============

* Don't use new HTML5 elements/tags and API.

* Don't use deprecated HTML4 elements/tags.

* Paragraphs of text should always be placed in a <p> tag.
  Never use multiple <br/> tags.

* Items in list form should always be in <ul>, <ol>, or <dl>,
  Never a set of <div> or <p>

* Every form input that has text attached should utilize a <label> tag.
  Especially radio or checkbox elements.

* Use double quotes for tag/element attributes.

* Even though using quotes around attributes is optional, always put quotes around
  attributes for readability::

GOOD: 
```html
    <p class="line note" data-attribute="106">
            This is my paragraph of special text.</p>
```
BAD:
```html
    <p class="line note" data-attribute=106>
            This is my paragraph of special text.</p>
```

* Make use of <thead>, <tfoot>, <tbody>, and <th> tags (and Scope attribute)
  when appropriate. (note: <tfoot> goes above <tbody> for speed reasons.
  You want the browser to load the footer before a table full of data.)::
```html
    <table summary="This is a chart of invoices for 2011.">
      <thead>
        <tr>
          <th scope="col">Table header 1</th>
          <th scope="col">Table header 2</th>
        </tr>
      </thead>
      <tfoot>
        <tr>
          <td>Table footer 1</td>
          <td>Table footer 2</td>
        </tr>
      </tfoot>
      <tbody>
        <tr>
          <td>Table data 1</td>
          <td>Table data 2</td>
        </tr>
      </tbody>
    </table>
```