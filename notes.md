##Part2.D.2
- 参数分为*位置参数（Positional Arguments，arg）*和*关键词参数(Keyword Arguments，kwarg)*两种。在函数定义中带有 = 、默认值的参数就是Keyword Arguments，其他的是Positional Arguments。
- 定义函数时，参数的顺序：
    - Positional
    - Arbitrary Positional
    - Keyword
    - Arbitrary Keyword
###Positional Arguments
- 如果位置参数前面标注了\*，这个参数就是“Arbitrary Positional Arguments”，可以接收一系列值
- 调用参数的时候，可以将一个容器传递给Arbitrary Positional Arguments，方法是调用时在参数前面加\*
- Arbitrary Positional Arugument只能有一个，应该位于其他Positional Argument之后

###Keyword Arguments
- 如果参数面前带\*\*，则是“Arbitrary Keyword Arguments”

##Part.2.D.3
- 为函数取化名是为了提高代码可读性

###lambda
- lambda_expr ::= "lambda" [parameter_list] ":" expression
    - 作为某函数的返回值
    - 作为某函数的参数