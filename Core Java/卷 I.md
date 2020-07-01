# 基础知识

## Ch01 概述

1. Java的核心特点

   1. 简单性

   2. 面向对象

      对象和对象的接口

   3. 分布式

      网络/分布式环境

   4. 健壮性

   5. 安全性

   6. 体系结构中立

      虚拟机

   7. 多线程
   8. 动态性

## Ch03 基本程序设计结构

<img src="%E5%8D%B7%20I/image-20200630150400023.png" alt="image-20200630150400023" style="zoom:50%;" />



如果在数值计算中不允许有任何舍入误差，就应该使用 BigDecimal 类。

<img src="%E5%8D%B7%20I/image-20200630151017121.png" alt="image-20200630151017121" style="zoom:50%;" />



整型值和布尔值之间不能进行相互转换。

逐一声明变量比较合适。

利用关键字**final**表示常量，常量名最好全大写。



**静态方法？**

<img src="%E5%8D%B7%20I/image-20200630152158315.png" alt="image-20200630152158315" style="zoom:50%;" />



floorMod 用来同余

<img src="%E5%8D%B7%20I/image-20200630152518319.png" alt="image-20200630152518319" style="zoom:50%;" />



boolean  b? 1:0

**枚举类型**



<img src="%E5%8D%B7%20I/image-20200630205545993.png" alt="image-20200630205545993" style="zoom:50%;" />



<img src="%E5%8D%B7%20I/image-20200630225435946.png" alt="image-20200630225435946" style="zoom:50%;" />



带标签的break语句

<img src="%E5%8D%B7%20I/image-20200630230907315.png" alt="image-20200630230907315" style="zoom:50%;" />

<img src="%E5%8D%B7%20I/image-20200630231210724.png" alt="image-20200630231210724" style="zoom:50%;" />

Java没有提供运算符重载功能

**数组长度为 0 与 null 不同。**

Java 中的 [ ] 运算符被预定义为检查数组边界， 而且没有指针运算， 即不能通过 a 加 1 得到数组的下一个元素

多维数组：数组的数组



## Ch04   对象与类

OOP：规模较大

- 对象的行为

- 对象的状态

- 对象标识

  如何辨别具有相同行为与状态的不同对象

类（class）构造（construct）<u>对象</u>的过程称为创建类的实例（instance）

封装（encapsulation）

对象中的数据：实例域（instance field） 		——> 状态

操纵数据的过程：方法（method）

**实现封装的关键**：绝对不能让类中的方法**直接**的访问其他类的实例域，程序仅通过对象的方法与数据对象进行交互



编写OOP：首先从设计类开始，然后再往每个类中添加方法。识别类的简单规则是在分析问题的过程中寻找名词， 而方法对应着动词。



类之间的关系

- 依赖 uses-a
- 聚合 has-a
- 继承 is-a



更改器方法（mutator method）与访问器方法（accessor method）

对象是否被修改

强烈建议将实例域标记为private

隐式参数与显式参数，**this**

<img src="%E5%8D%B7%20I/image-20200701171159024.png" alt="image-20200701171159024" style="zoom:50%;" />

**不要编写返回引用<u>[可变对象](https://blog.csdn.net/bupa900318/article/details/80696785?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.compare&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.compare)</u>的访问器方法。**

Override



 Employee 类的方法可以访问 Employee 类 的任何一个对象的私有域

一个方法可以访问<u>所属类</u>的所有对象的私有数据，



final表示存储在变量中的对象引用不会再指示其他对象，但这个对象可以更改



<img src="%E5%8D%B7%20I/image-20200701223426299.png" alt="image-20200701223426299" style="zoom:50%;" />



[工厂方法](https://www.runoob.com/design-pattern/design-pattern-intro.html)



<img src="%E5%8D%B7%20I/image-20200701224930219.png" alt="image-20200701224930219" style="zoom:50%;" />



- 方法参数
  - 按值调用 ->基本数据类型
  - 按引用调用 ->对象引用



<img src="%E5%8D%B7%20I/image-20200702000624751.png" alt="image-20200702000624751" style="zoom:50%;" />

<img src="%E5%8D%B7%20I/image-20200702001143658.png" alt="image-20200702001143658" style="zoom:50%;" />

<img src="%E5%8D%B7%20I/image-20200702001351085.png" alt="image-20200702001351085" style="zoom:50%;" />



<img src="%E5%8D%B7%20I/image-20200702002129885.png" alt="image-20200702002129885" style="zoom:50%;" />

如果使用静态方法就需要加 static



### 类设计技巧

1. 一定要保证数据私有，不要破坏封装性

2. 一定要对数据初始化

3. 不要在类中使用过多的基本类型

   <img src="%E5%8D%B7%20I/image-20200702010939863.png" alt="image-20200702010939863" style="zoom:50%;" />

4. 不是所有的域都需要独立的域访问器/更改器
5. 将职责过多的类进行分解
6. 类名和方法名要能够体现其职责
7. 优先使用不可变的类