/**
 * Created by huang on 2018/6/21.
 **/
$(function () {
    homeJs.getLabel();
    homeJs.display_article();
});


var homeJs = {
    getLabel: function () {
        $.ajax({
            url: '/blog/home/get_label_info',
            type: 'get',
            success: function (data) {
                var str_label = '';
                var lable_list = methodsFun.dic_with(data.data);
                for (i = 0; i < lable_list.length/2; i++) {
                    str_label = str_label+'<li class="list-group-item d-flex justify-content-between align-items-center">'+
                        lable_list[i*2+1]+'<span class="badge badge-primary badge-pill">'+lable_list[i*2]+'</span>'+'</li>';
                }
                $('#list_group').html(str_label);
            }

        })
    },

    display_article:function () {
        $.ajax({
            url: '/blog/home/get_article_info',
            type: 'get',
            success:function (data) {
                var article_info = data.data;

                for (var i=0;i<article_info.length;i++){
                    $('#abc').html(article_info[i]['article_content']);
                    console.info(article_info[i]['article_content']);
                }

            }
        });

    }
};


var methodsFun = {
    dic_with: function (data) {
        // 将对象转换成list
        var label_list = [];
        for ( var v in data) {
            var a = data[v];
            for (var b in a) {
                label_list.push(a[b]);
                label_list.push(b);
            }
        }
        return label_list;
    }
};