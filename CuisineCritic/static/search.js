window.onload = () => {
    document.getElementById('search').addEventListener('submit', (e) => {
        e.preventDefault();
        var search = document.getElementById('query').value;
        
        if (search == "") {
            //send_search_alert("Please enter a search term.");
        } else {
            // fetch /api/search
            fetch('/api/search', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector(["[name=csrfmiddlewaretoken]"]).value
                },
                body: new FormData(document.getElementById("search")),
            })
            .then(res => res.json())
            .then(res => {
                if(res.success) {
                    // display results
                    var html = "We found the following restaurant(s):";
                    html += `<ul class="list-group mt-3">`;
                    for (var i = 0; i < res.restaurants.length; i++) {
                        html += `<li class="list-group-item"><a href="/restaurants/${res.restaurants[i].slug}">${res.restaurants[i].name}</a></li>`;
                    }
                    html += `</ul>`;
                    send_search_alert(html, false);
                    
                } else {
                    send_search_alert(res.message);
                }
            })
            .catch(err => {
                console.log(err);
                send_search_alert("An unexpected error occurred.");
            });
        }
    });
};

function send_search_alert(html, danger=true) {
    if (danger) {
        html = `<span class="text-danger">${html}</span>`;
    }
    document.getElementById('search-response').innerHTML = html;

    var modal = new bootstrap.Modal(document.getElementById("search-modal"), {});
    modal.show();

    if(danger) {
        setTimeout(
            function() {
                modal.hide();
            }, 2000
        );
    }
}