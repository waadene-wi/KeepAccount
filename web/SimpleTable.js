/**
 * 簡單表格
 */

function SimpleTable(column_count, table_id=null) {
    this.column_count = column_count;
    this.header = null;
    this.row = [];
    this.id = table_id;

    this.setHeader = function(header) {
        if(header.length != this.column_count) {
            throw 'column_count not match!';
        }
        this.header = header;
    }

    this.addRow = function(row) {
        if(row.length != this.column_count) {
            throw 'column_count not match!';
        }
        this.row.push(row);
    }

    this.show = function(father_id) {
        table = document.createElement('table');
        if(this.id != null) {
            table.id = this.id;
        }
        table.border = 1;
        // 設置表頭
        if(this.header != null) {
            table_row = document.createElement('tr');
            this.header.forEach(function(str) {
                cell = document.createElement('th');
                cell.innerHTML = str;
                table_row.appendChild(cell);
            });
            table.appendChild(table_row);
        }
        // 添加內容
        this.row.forEach(function(row){
            table_row = document.createElement('tr');
            row.forEach(function(str){
                cell = document.createElement('td');
                cell.innerHTML = str;
                table_row.appendChild(cell);
            });
            table.appendChild(table_row);
        });
        document.getElementById(father_id).appendChild(table);
    }
}
