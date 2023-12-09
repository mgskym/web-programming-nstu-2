function fillCourseList() {
    fetch('lab8/api/courses')
    .then(function(data) {
        return data.json();
    })
    .then(function(courses) {
        let  tbody = document.getElementById('course-list');
        tbody.innerHTML = '';
        for(let i = 0; i < courses.length; i++) {
            tr = document.createElement('tr');
            let tdName = document.createElement('td');
            let tdVideos = document.createElement('td');
            let tdPrice = document.createElement('td');
            let tdActions = document.createElement('td');

            tr.append(tdName);
            tr.append(tdVideos);
            tr.append(tdPrice);
            tr.append(tdActions);

            tbody.append(tr);
        }
    })
};