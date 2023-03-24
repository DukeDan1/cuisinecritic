window.onload = () => {
    form_fixer();

    document.getElementById('add-restaurant').addEventListener('submit', (e) => {
        e.preventDefault();
        
        button_disable(true);
        var form = new FormData(document.getElementById("add-restaurant"));
        form.delete('restaurant-image');

        var resElement =  document.getElementById('response');
        if(document.getElementById('restaurant-image').files.length < 1) {
            resElement.innerHTML = generateAlert('Please upload at least one image.', 'danger');
            button_disable(false);
            return;
        }

        fetch('/api/create_restaurant', {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector(["[name=csrfmiddlewaretoken]"]).value
            },
            body: form,
        }).then(res => res.json())
        .then(data => {
            
            
            if(data.success) {
                
                // Submit profile image
                var element = document.querySelector('#restaurant-image');
                if (element.files.length > 0) {
                    var formData = new FormData();
                    for(var i = 0; i < element.files.length; i++) {
                        formData.append(`restaurant-image${i}`,element.files[i]);
                    }
                    
                    var newCSRFToken = document.cookie.split(';').find(row => row.trim().startsWith('csrftoken')).split('=')[1];

                    formData.append('csrfmiddlewaretoken', newCSRFToken);
                    formData.append('restaurant_id', data.restaurant_id);

                    fetch('/api/upload_restaurant_image', {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken':newCSRFToken
                        },
                        body: formData,
                    }).then(res => res.json())
                    .then(imageResponse => {
                        button_disable(false);
                        if (imageResponse.success) {
                            resElement.innerHTML = generateAlert(data.message, 'success');
                        } else {;
                            resElement.innerHTML = generateAlert(imageResponse.message, 'danger');
                        }
                    })
                    .catch(err => {
                        console.log(err);
                        button_disable(false);
                        resElement.innerHTML = generateAlert("Something went wrong. Please retry.");
                    });
                } else {
                    button_disable(false);
                    resElement.innerHTML = generateAlert(data.message, 'success');
                }

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
        btn.innerHTML = "Add Restaurant";
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

    document.querySelector("select").classList.add("form-select", "mt-3", "mb-3");
    document.querySelector(`[for=id_category]`).remove();
    document.querySelector("select").options[0].innerHTML = "Select a restaurant type...";

    document.querySelector("#restaurant-image").outerHTML = `<label for="restaurant-image" class="form-label">Choose some image(s) for your restaurant:</label>` + document.querySelector("#restaurant-image").outerHTML;

    Array.from(document.getElementsByClassName('helptext')).forEach(e => e.classList.add('d-none', 'text-light'));
    Array.from(document.querySelector('#add-restaurant').getElementsByTagName("br")).forEach(e => e.remove());
}