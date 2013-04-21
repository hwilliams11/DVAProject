/*Parameters:
    callback - function that will be called with the data. This methos is asynchronous.

Returns a javascript array of expenses. A sample expense looks like - 
    {
      "eid": 1691,
      "description": "Getty",
      "amount": 59,
      "category": "transportation",
      "date": "2013-09-18T04:00:00.000Z",
      "user_data": [
        {
          "eid": 1691,
          "uid": 2,
          "paid": 41.3,
          "share": 59
        },
        {
          "eid": 1691,
          "uid": 1,
          "paid": 17.7,
          "share": 59
        }
      ]
    }

*/
function getData(callBack) {
    var format_old = d3.time.format("%Y-%m-%d");
    var format = d3.time.format("%m/%d/%Y");
    d3.tsv('data/expense_table.txt')
        .row(function(d) { return {eid: +d.eid, description: d.description, 
                                   amount: +d.amount, category: d.category=="None"?null:d.category, 
                                   date: format.parse(d.date)}; 
                         })
        .get(function(error, exp_rows) { 
            d3.tsv('data/expense_user_table.txt')
            .row(function(d) {
                return {eid:+d.eid, uid:+d.uid, paid:+d.paid, share:+d.share};
            })
            .get(function(error, exp_user_rows) {
                 var exp_user_map = d3.nest()
                    .key(function(d) { return d.eid; })
                    .map(exp_user_rows, d3.map);
                 var combined_data = exp_rows.map(function(row) {row.user_data = exp_user_map.get(row.eid); return row;})
                 callBack(combined_data); 
            });
        });
};
    
