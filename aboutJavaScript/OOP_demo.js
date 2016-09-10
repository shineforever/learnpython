/**
 * Created by qimi on 2016/9/10.
 */
// 面向对象的一些代码片段


// 构造函数，首字母大写（与普通函数对比）
function Student(props) {
    this.name = props.name || "匿名";
    this.grade = props.grade || 1;
}

Student.prototype.hello = function () {
    alert("Hello, "+this.name+"!");
};

// 额外定义一个创建Student的函数
function createStudent(props) {
    return new Student(props);
}

var xiaoming = new Student("小明");
console.log(xiaoming.name);
xiaoming.hello();

function PrimaryStudent(props) {
    // 调用Student构造函数，绑定this变量
    Student.call(this, props);
    this.grade = props.grade || 1;
}

// 空函数
function F() {
}

//把F的原型指向Student.prototype
F.prototype = Student.prototype;

//把PrimaryStudent的原型指向一个新的P对象，F对象的原型正好指向Student.prototype
PrimaryStudent.prototype = new F();

//把PrimaryStudent原型的构造函数修复为PrimaryStudent
PrimaryStudent.prototype.constructor = PrimaryStudent;

// 继续在PrimaryStudent原型(就是new F()对象)上定义方法
PrimaryStudent.prototype.getGrade = function () {
    return this.grade;
};


// 客服用的继承函数
function inherits(Child, Parent) {
    var F = function () {};
    F.prototype = Parent.prototype;
    Child.prototype = new F();
    Child.prototype.constructor = Child;
}

// ES6的Promise
// 生成一个0-2之间的随机数，如果小于1，则等待一段时间后返回成功，否则返回失败
function test(resolve, reject) {
    var timeOut = Math.random() * 2;
    console.log("set timeout to "+timeOut+"seconds");
    setTimeout(function () {
        if (timeOut < 1) {
            console.log("call resolve()...");
            resolve("200 ok");
        }
        else {
            console.log("call reject()...");
            reject("timeout in "+timeOut+"seconds");
        }
    }, timeOut*1000);
}

var p1 = new Promise(test);
var p2 = p1.then(function (result) {
    console.log("成功："+result);
});
var p3 = p1.catch(function (reason) {
    console.log("失败："+reason);
});
