<div class="problemQuestion">
<p><span style="font-size:18px">You are given two objects. Each object has data members X, Y and Z.<br>
You need to find the nth Fibonacci object. The nth Fibonacci object is given by F(n) = F(n - 1) + F(n - 2); n &gt; 2<br>
You need to sum the corresponding values of obj1 and obj2 to get obj3.</span></p>

<p><span style="font-size:18px"><strong>Examples:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
For obj1: X = 1, Y = 2, Z = 3
For obj2: X = 4, Y = 5, Z = 6
n = 4</span>
<span style="font-size:18px"><strong>Output:</strong>
9 12 15</span>
<strong><span style="font-size:18px">Explanation:</span></strong>
<span style="font-size:18px">obj1: X = 1, Y = 2, Z = 3</span>
<span style="font-size:18px">obj2: X = 4, Y = 5, Z = 6</span>
<span style="font-size:18px"><strong>For n == 1</strong> return obj1</span>
<span style="font-size:18px"><strong>For n == 2</strong> return obj2</span>
<span style="font-size:18px"><strong>For n == 3</strong> return obj1 + obj2 (5 , 7, 9)</span>
<span style="font-size:18px">temp = obj2 (4, 5, 6)</span>
<span style="font-size:18px">obj2  = obj1 + obj2 (5, 7, 9)</span>
<span style="font-size:18px">obj1 = temp (4, 5, 6)</span>
<span style="font-size:18px"><strong>For n == 4</strong> return obj1 + obj2 (9, 12, 15)</span>
<span style="font-size:18px">temp = obj2 (5, 7, 9)</span>
<span style="font-size:18px">obj2  = obj1 + obj2 (9, 12, 15)</span>
<span style="font-size:18px">obj1 = temp (5, 7, 9)</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
This is a function problem, you don't need to read/print anything. Just complete the function <strong>nthFibO() </strong>and return the object<strong>.</strong></span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= X, Y, Z&nbsp;&lt;= 10<sup>4</sup></span></p>
</div>