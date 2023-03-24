window.onload = () => {
    document.getElementById('review-form').addEventListener('submit', (e) => {
        e.preventDefault();

        button_disable(true);
        fetch('/api/review', {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector(["[name=csrfmiddlewaretoken]"]).value
            },
            body: new FormData(document.getElementById("review-form")),
        }).then(res => res.json())
        .then(data => {
            var resElement =  document.getElementById('response');
            
            if(data.success) {
                resElement.innerHTML = generateAlert(data.message, 'success');
                document.getElementById('submit').classList.replace('btn-info', 'btn-success');
                document.getElementById('submit').innerHTML = 'Submitted';
                document.getElementById('close-modal').innerHTML = "Close";
                document.getElementById('close-modal').classList.replace('btn-danger', 'btn-primary');
            } else {
                button_disable(false);
                resElement.innerHTML = generateAlert(data.message);
            }
        })
        .catch(err => {
            console.log(err);
            button_disable(false);
            document.getElementById('response').innerHTML = generateAlert("Something went wrong. Please retry.");
        });
    });

    function button_disable(enable) {
        var btn = document.getElementById('submit');
        if (!enable) {
            btn.disabled = false;
            btn.classList.replace("btn-info", "btn-success");
            btn.innerHTML = "Submit";
        } else {
            btn.disabled = true;
            btn.classList.replace("btn-success", "btn-info");
            btn.innerHTML = "Submitting...";
        }
    }

    window.enabled_form = false;
    document.querySelectorAll("input").forEach((input) => {
        input.addEventListener("keyup", (e) => {
            if(!window.enabled_form) {
                document.getElementById('submit').disabled = false;
                window.enabled_form = true;
            }
        });
    });
};