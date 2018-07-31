/**
 * Created by huang on 2018/6/21.
 **/
$(function () {
    homeJs.getLabel();
});


var homeJs = {
    getLabel: function () {
        $.ajax({
            url: '/blog/home/get_label',
            type: 'post',
            success: function (data) {
                var str_label = '';
                var str_lable_k = [];
                var str_lable_v = [];

                var lable_list = methodsFun.dic_with(data.info);
                for (i = 0; i < lable_list.length/2; i++) {
                    str_label = str_label+'<li class="list-group-item d-flex justify-content-between align-items-center">'+
                        lable_list[i*2+1]+'<span class="badge badge-primary badge-pill">'+lable_list[i*2]+'</span>'+'</li>';
                }
                $('#list_group').html(str_label);
            }

        })
    }
};


var methodsFun = {
    dic_with: function (data) {
        // 将对象转换成list
        var label_list = [];
        for (v in data) {
            var a = data[v];
            for (b in a) {
                label_list.push(a[b]);
                label_list.push(b);
            }
        }
        return label_list;
    }
};