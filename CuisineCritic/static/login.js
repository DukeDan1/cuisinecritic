window.onload = () => {
    document.getElementById('login').addEventListener('submit', (e) => {
        e.preventDefault();

        
        button_disable(true);
        fetch('/api/login', {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector(["[name=csrfmiddlewaretoken]"]).value
            },
            body: new FormData(document.getElementById("login")),
        }).then(res => res.json())
        .then(data => {
            var resElement =  document.getElementById('response');
            if(data.success) {
                resElement.innerHTML = generateAlert(data.message, 'success');
                setTimeout(() => {
                    window.location.href = '/restaurants';
                }, 500);
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
};

function button_disable(enable) {
    var btn = document.getElementById('submit');
    if (!enable) {
        btn.disabled = false;
        btn.classList.replace("btn-info", "btn-light");
        btn.innerHTML = "Log in";
    } else {
        btn.disabled = true;
        btn.classList.replace("btn-light", "btn-info");
        btn.innerHTML = "Submitting...";
    }
}