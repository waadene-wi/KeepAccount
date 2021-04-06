function getUrlAsyn(url, onReturn200Callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4) {
            if(xhr.status == 200) {
                onReturn200Callback(xhr.responseText);
            }
        }
    }    
    xhr.timeout = 2000; // ms
    xhr.send();
}

// 获取年月日时分字符串
// offset表示要获取的时间与当前时间的差值，单位为毫秒
function getDateTimeString(offset_ms=0) {
    var date;
    if(offset_ms == 0) {
        date = new Date();
    }
    else {
        var ts = Date.parse(new Date());
        ts += offset_ms;
        date = new Date(ts);
    }
    Y = date.getFullYear();
    M = date.getMonth() + 1;
    D = date.getDate();
    h = date.getHours();
    m = date.getMinutes();
    if(M < 10) { M = '0' + M;}
    if(D < 10) { D = '0' + D;}
    if(h < 10) { h = '0' + h;}
    if(m < 10) { m = '0' + m;}
    return Y + '-' + M + '-' + D + ' ' + h + ':' + m;
}

// 清空選項菜單的所有選項
function select_clearOptionsByClassname(select_ele, opt_class) {
    options =  select_ele.getElementsByClassName(opt_class);
    while(true) {
        opt = options.item(0);
        if(opt == null) {
            break;
        }
        select_ele.removeChild(opt);
    }
}

// 向選項菜單中追加一個選項
function select_appendOption(select_ele, val, text, class_name) {
    opt = document.createElement('option')
    opt.text = text;
    opt.value = val;
    opt.className = class_name;
    select_ele.appendChild(opt);
}
