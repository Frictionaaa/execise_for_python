#运用字典实现加减乘除

from __future__ import division
x=1
y=2
operator="/"
multpily="^"
result={
      "+":x+y,
      "-":x-y,
      "*":x*y,
      "/":x/y,
      "^":y*y
}
abs=result.get(operator)
mul=result.get(multpily)
print(abs)
print(mul)