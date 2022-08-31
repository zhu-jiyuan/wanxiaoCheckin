
# 完美校园打卡
## 日志
  - ⚡ Python3.8
  - 🍻 只需要一个完美校园的账号和密码就可以给全校人打卡.
  - 🖋 健康打卡数据请自行爬虫（十分建议）或手动添加到打卡数据.txt中，manage.py是管理打卡的（也可以在数据管理中自行添加）。
  - 🥋 河南师范大学可以稳定使用。请使用云函数或者服务器定时任务执行此脚本，github的fork不稳定。
  - ♟ python一点都不会的，建议不折腾，好好学习，坐等现成。
  - 📫 联系方式[QQ](https://qm.qq.com/cgi-bin/qm/qr?k=B7K2xJ4K3zz8z8qek7gWfulyuel_XtGS&noverify=0)
## 打卡的几个问题以及解决方案

### 1，模拟登录问题（核心问题）

​	通过对完美校园app的逆向分析，模拟登录问题已经迎刃而解，如果想要自己分析，可以在豌豆荚内下载低版本的apk(因为，低版本没有360加固)，在这里很感谢[@zhongbr](https://github.com/zhongbr)前辈所做的逆向分析，令我学到了很多也省去了不少分析时的麻烦，同时还有感谢[@ReaJason](https://github.com/ReaJason)学长和他的朋友对验证码登录逆向分析，很方便的解决唯一识别符的问题。

​	PS：逆向分析是非常枯燥无味的，要求有java基础等，起初我在进行分析时，毫无头绪，学了将近一个月的java花了一天的时间才搞懂完美校园登录逆向分析。同时我想对不熟悉java的同学说：“太浪费时间了，快去学习，现在就是读书太少，想的太多。”

### 2，打卡的一些问题

#### 	1，多人打卡问题

​			关于多人打卡问题，我的解决方案是先把需要打卡的人的信息放入MySQL或者一个json、txt文件存储，用一个账号token先调用更改打卡用户信息的接口，改变用户，再进行打卡。

#### 	2，打卡信息的获取问题

​			不管你会不会抓包，获取打卡信息都是一件麻烦事，我这里写了一个接口，但是没有界面化，这里由于开学要考试的原因，十分抱歉，暂时不上传了。

​			最简单的就是通过登录个人的账号，通过token获取到上次打卡的个人信息。但是需要通过验证码登录。

​			最近对HTML，JavaScript非常感兴趣，有前端基础的同学，可以做一个前端，这样就可以彻底解决了。

#### 	3，不同学校的打卡问题

​			很抱歉，不同学校打卡post请求提交的数据是不一样的，这就使得统一全国打卡的python版本需要收集更多的数据，通过提交表单的不同，进行分类。

​			JavaScript能够很好解决这个问题，但是需要不同账号的token。

### 3，该代码仓库以及如何使用它

​	该代码是我为了应付学校的一些形式主义，不得已才写的，仅供个人使用，但随着自己越来越懒，我开始不断完善代码，现在有python基础的同学以及可以使用了。代码起初直接就是自己的数据，现在可以是任何人的，但是我还是不会去完善它的，也不会给它做图形页面来自动生成可以部署到云函数或者服务器的代码。

​	打卡应该快结束了，毕竟形式主义不是好事儿，打卡也预防不了病毒，开学之后，希望学完JavaScript和html之后可以写出web版，更方便自己的使用，同时也可以让大家用到。

​	维护全国打卡，太浪费时间了，我仅维护河南师范大学的打卡。以方便大家更好的生活，去解决生活中的小麻烦。



<h6>* 大二物理专业，学习比较紧张，如果你也喜欢编程方便生活or数学等，可以联系我哦</h6>
