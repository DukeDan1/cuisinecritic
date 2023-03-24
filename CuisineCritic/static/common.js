function generateAlert(msg, type='danger') {
    return `
    <div class="alert alert-${type} alert-dismissible fade show" role="alert">
        <strong> ${msg} </strong>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    `;
}

