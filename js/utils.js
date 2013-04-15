function getData(callBack) {
    var format = d3.time.format("%Y-%m-%d");
    d3.tsv('data/expense_table.txt')
        .row(function(d) { return {id: +d.id, description: d.description, 
                                   amount: +d.amount, category: d.category=="None"?null:d.category, 
                                   date: format.parse(d.date)}; 
                         })
        .get(function(error, exp_rows) { 
            d3.tsv('data/expense_user_table.txt')
            .row(function(d) {
                return {id:+d.id, user_id:+d.user_id, paid:+d.paid, share:+d.share};
            })
            .get(function(error, exp_user_rows) {
                 var exp_user_map = d3.nest()
                    .key(function(d) { return d.id; })
                    .map(exp_user_rows, d3.map);
                 var combined_data = exp_rows.map(function(row) {row.user_data = exp_user_map.get(row.id); return row;})
                 callBack(combined_data); 
            });
        });
};
    
