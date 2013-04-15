/*Parameters:
    callback - function that will be called with the data. This methos is asynchronous.

Returns a javascript array of expenses. A sample expense looks like - 
    {
      "id": 109,
      "description": "Walmart Commons",
      "amount": 20.68,
      "category": null,   (null because none assigned right now)
      "date": "2013-04-10T04:00:00.000Z",  (javascript data object)
      "user_data": [    (array of expense_user entries for this expense)
        {
          "id": 109,
          "user_id": 1,
          "paid": 20.68,
          "share": 6.89
        },
        {
          "id": 109,
          "user_id": 2,
          "paid": 0,
          "share": 6.9
        },
        {
          "id": 109,
          "user_id": 3,
          "paid": 0,
          "share": 6.89
        }
      ]
    }
*/
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
    
