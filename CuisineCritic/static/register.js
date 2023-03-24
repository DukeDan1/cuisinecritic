window.onload = () => {
    form_fixer();

    document.getElementById('register').addEventListener('submit', (e) => {
        e.preventDefault();
        
        button_disable(true);
        var form = new FormData(document.getElementById("register"));
        form.delete('avatar_src');

        fetch('/api/register', {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector(["[name=csrfmiddlewaretoken]"]).value
            },
            body: form,
        }).then(res => res.json())
        .then(data => {
            var resElement =  document.getElementById('response');
            button_disable(false);
            if(data.success) {
                
                // Submit profile image
                var element = document.querySelector('[name=avatar_src]');
                if (element.files.length > 0) {
                    var formData = new FormData();
                    formData.append('avatar_src',element.files[0]);
                    var newCSRFToken = document.cookie.split(';').find(row => row.trim().startsWith('csrftoken')).split('=')[1];

                    formData.append('csrfmiddlewaretoken', newCSRFToken);

                    fetch('/api/upload_avatar', {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken':newCSRFToken
                        },
                        body: formData,
                    }).then(res => res.json())
                    .then(imageResponse => {
                        if (imageResponse.success) {
                            resElement.innerHTML = generateAlert(data.message, 'success');
                        } else {
                            data.message += " But profile image upload failed.";
                            resElement.innerHTML = generateAlert(data.message, 'success');
                        }

                        setTimeout(() => {
                            window.location.href = '/restaurants';
                        }, 2000);
                    })
                    .catch(err => {
                        console.log(err);
                        resElement.innerHTML = generateAlert("Something went wrong. Please retry.");
                    });
                } else {
                    resElement.innerHTML = generateAlert(data.message, 'success');
                    setTimeout(() => {
                        window.location.href = '/restaurants';
                    }, 2000);
                }

            } else {
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
        btn.innerHTML = "Register";
    } else {
        btn.disabled = true;
        btn.classList.replace("btn-light", "btn-info");
        btn.innerHTML = "Submitting...";
    }
}



function form_fixer() {
    // Add bootstrap classes to form elements
    var elements = document.getElementsByTagName('input');
    var label;
    for (var i = 0; i < elements.length; i++) {
        if (elements[i].type == 'text' || elements[i].type == 'password' || elements[i].type == "email" || elements[i].type == "file") {
            elements[i].classList.add('form-control', 'mt-3', 'mb-3');
            label = document.querySelector(`[for="${elements[i].id}"]`);
            elements[i].placeholder = label.innerHTML.replace(":", "");
            label.remove();
        }
    }

    document.querySelector("[name=avatar_src]").outerHTML = `<label for="avatar_src" class="form-label">Choose a profile picture:</label>` + document.querySelector("[name=avatar_src]").outerHTML;

    Array.from(document.getElementsByClassName('helptext')).forEach(e => e.classList.add('d-none', 'text-light'));
    Array.from(document.querySelector('#register').getElementsByTagName("br")).forEach(e => e.remove());
}