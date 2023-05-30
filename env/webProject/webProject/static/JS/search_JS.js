let status =  document.querySelector("select");
let id_student = document.querySelector(".student_id");
let table  = document.querySelector("table");


let search = document.querySelector(".search");

search.addEventListener("click",()=>{
     let id = id_student.value;
     let status_value = status.value;

     if(id!="" && status_value!=""){
             req = new XMLHttpRequest();
             req.onreadystatechange= ()=>{
              if(req.readyState == 4 && req.status == 200 ){
                 if(req.response!=""){
                       let content_table = "<tr id ='head_tr'><th>Name</th><th>ID</th><th>Department</th>";
                       let data = JSON.parse(req.response);
                       data.forEach((student)=>{
                            content_table+=`
                                      <tr>
                                      <td>${student.name}</td>
                                      <td>${student.id}</td>
                                      <td>${student.department}</td>

                                  </tr>
                            `;


                       });
                       table.innerHTML = content_table;

                 }else{

                      table.innerHTML = "no results";
                  }

              }
             };
             req.open("GET",'search_ajax?id='+id+"&"+"status="+status_value);
             req.send();
     }


})


