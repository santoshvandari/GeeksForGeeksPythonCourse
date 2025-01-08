<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are given a string <strong>str</strong> that contains some Html text. In this Html text is an image URL that is in the tag. You need to extract the URL. The image URL is of the format .jpg.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
&lt;html&gt;&lt;head&gt;&lt;/head&gt;&lt;body&gt;&lt;img src='www.geeksforgeeks.org/sample/62.jpg'&lt;/body&gt;&lt;/html&gt;
<strong>Output:</strong>
www.geeksforgeeks.org/sample/62.jpg</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
&lt;html&gt;&lt;head&gt;&lt;/head&gt;&lt;body&gt;&lt;img src='www.geeksforgeeks.org/sample/99.jpg'&lt;/body&gt;&lt;/html&gt;
<strong>Output:</strong>
www.geeksforgeeks.org/sample/99.jpg</span>
</pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
This is a function problem. Do not take any input. Just complete the function <strong>imgExtracter()&nbsp;</strong>and print the output.</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= |str|&nbsp;&lt;= 10<sup>5</sup></span></p>
</div>