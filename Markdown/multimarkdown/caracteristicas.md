MultiMarkdown 2.0 utilizó **ASCCIMathML** para componer ecuaciones matemáticas. El uso de **ASCCIMathML** tenía ventajas, pero también algunas desventajas. 


Al reescribirse MultiMarkdown 3.0, no había una forma sencilla de implementar **ASCCIMathML**, lo que llevó a buscar alternativas. Se termino por usar **MathJax**. la ventaja aquí es que **MathJax** admite la misma sintaxis de los navegadores y en la sintaxis nativa














Tablas

<pre><code class="hljs ruby">
<span class="hljs-params">|             |</span>          Grouping           <span class="hljs-params">||</span>
First Header  <span class="hljs-params">| Second Header |</span> Third Header <span class="hljs-params">|
 ------------ |</span> <span class="hljs-symbol">:-----------</span>: <span class="hljs-params">| -----------: |</span>
Content       <span class="hljs-params">|          *Long Cell*        |</span><span class="hljs-params">|
Content       |</span>   **Cell**    <span class="hljs-params">|         Cell |</span><font></font>
<font></font>
New section   <span class="hljs-params">|     More      |</span>         Data <span class="hljs-params">|
And more      |</span> With an escaped <span class="hljs-string">'\|'</span>         <span class="hljs-params">||</span>  <font></font>
[Prototype table]<font></font>
<font></font>
</code></pre>