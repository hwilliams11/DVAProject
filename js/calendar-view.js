
function showData() {
    $("#main_box_init").hide();
    $("#main_box").show();
    var usr_map = d3.map();
    usr_map.set(1, "John");
    usr_map.set(2, "Rob");
    usr_map.set(3, "Bob");
    usr_map.set(4, "Matt");
    var bdate_format = d3.time.format("%b %d, %Y");
    var id = parseInt($(this).attr("id").split("_")[1]);
    console.log(id);
    var exp = expenseDict.get(id);
    $("#box_date").html(bdate_format(exp.date));
    $("#box_desc").html(exp.description);
    $("#box_amt").html("$"+exp.amount);
    $("#box_categ").html(toTitle(exp.category));
    var tab_html = "";
    exp.user_data.forEach(function(d) {
        tab_html += "<tr><td>{{user}}</td><td>{{paid}}</td><td>{{share}}</td></tr>".replace("{{user}}", usr_map.get(d.uid))
                        .replace("{{paid}}", "$"+d.paid).replace("{{share}}",  "$"+d.share)
        console.log(tab_html);
    });
    $("#box_users tbody").html(tab_html);
    
}

function toTitle(str)
{
    return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
}

function renderExpenses(expense_rows, mm, yy) {
    console.log(mm, yy);
     
    var box_template = '<div class="expense_box" style="clear:both;"><div class="scrollable"></div></div>';
    var template  = '<div id="expense_{{id}}" class="expense-blue" >' +
                        '<strong style="float:left;width:40px;">${{amount}}</strong>{{description}}' +
                        '<i style="float:right;margin-right:2px;margin-top:2px;" class="{{category}}"></i>' +
                    '</div>';

    var tot_template  = '<div class="expense-total" >' +
                            '<strong style="float:left;width:40px;">${{amount}}</strong>Total' +
                            '<i style="float:right;margin-right:2px;margin-top:2px;" class="icon-ok"></i>' +
                        '</div>';


    expense_rows.filter(function(d) { return (d.key.getMonth() == mm && d.key.getFullYear() == yy); })
            .forEach(function(e) {
                if(e.values.length > 0) {
                    box = $(box_template).appendTo($("#day_"+e.key.getDate()));
                    e.values.forEach(function(e1){
                        var exp_pal = $(template.replace("{{id}}", ''+e1.eid)
                            .replace("{{amount}}", getAmountString(e1.amount))
                            .replace("{{description}}", getDescriptionString(e1.description))
                            .replace("{{category}}", getCategory(e1.category)))
                        .appendTo(box.find(".scrollable"));
                        if(e1.user_data.length > 1)
                            exp_pal.addClass("shared-expense");
                    });
                    if(e.values.length > 1) {
                        // total logic
                        var tot = d3.sum(e.values.map(function(d) { return d.amount; }));
                        $(tot_template.replace("{{amount}}", getAmountString(tot))).appendTo(box);
                    }
                }
            });
}

function getAmountString(amt) {
    if(amt < 10) {
        if(amt % 1 == 0 || amt * 10 % 1 == 0) 
            return "" + amt;
        else
            return "" + amt.toFixed(2);
    }
    else if(amt >= 10 && amt < 100) {
        if(amt % 1 == 0) 
            return "" + amt;
        else
            return "" + amt.toFixed(1);
    }
    else if(amt >= 100 && amt < 1000) {
        return "" + Math.round(amt);
    }
    else {
        var amtk = amt/1000.0
        if(amtk % 1 == 0 || amtk > 10)
            return "" + Math.round(amtk) + "k";
        else
            return "" + amtk.toFixed(1) + "k"
    }

}

function getDescriptionString(desc) {
    if(desc.length <= 13)
        return desc
    else
        return desc.slice(0,11) + "..";
}

function getCategory(categ_string) {

    switch(categ_string) {
        case 'grocery':
            return "icon-food";
        case 'shopping':
            return "icon-shopping-cart";
        case 'transportation':
            return "icon-truck";
        case 'entertainment':
            return "icon-magic";
        case 'home':
            return "icon-home";
        case 'utilities':
            return "icon-bolt";
        case 'special':
            return "icon-certificate";
        case 'restaurants':
            return "icon-glass";
    }

}