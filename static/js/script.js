$(document).ready(function() {
       
        
    var empDataTable = $('#empTable').DataTable({
                'processing': true,
                'serverSide': true,
                'serverMethod': 'post',
                'ajax': {
                    'url':'/ajaxfile'
                },
                'lengthMenu': [[5, 10, 25, 50, -1], [5, 10, 25, 50, "All"]],
                searching: true,
                sort: false,
                "serverSide": true,
                'columns': [
                    { data: 'replid' },
                    { data: 'nis' },
                    { data: 'nama' },
                    { data: 'tahunmasuk' },
                    { data: 'idangkatan' },
                    { data: 'idkelas' },
                    { data: 'kelamin' },
                    { data: 'pinsiswa' },
                    { data: 'pinortu' },
                    { data: 'pinortuibu' },
                ]
            });
 
});
 