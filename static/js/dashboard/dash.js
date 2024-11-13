document.addEventListener('DOMContentLoaded', function() {
    const scrollBtn = document.getElementById('scrollTopBtn');
    if (scrollBtn) {
        scrollBtn.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Set initial active state and load content if necessary
    const path = window.location.pathname;
    if (path === '/dashboard/' || path === '/dash/') {
        setActiveNavItem();
        loadContent('/dash/');  // Assuming you have a home view
    } else if (path.includes('/dash/')) {
        const model = path.split('/')[2];
        setActiveNavItem(model);
        loadModelList(model);
    }
});

function setActiveNavItem(model) {
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });
    
    if (!model || model === 'home') {
        document.querySelector('a.nav-item[href*="dashboard"]').classList.add('active');
    } else {
        const element = document.querySelector(`button.nav-item[onclick*="${model}"]`);
        if (element) {
            element.classList.add('active');
        }
    }
}

function loadContent(url) {
    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.getElementById('content').innerHTML = html;
        })
        .catch(error => console.error('Error loading content:', error));
}

function loadModelList(model) {
    loadContent(`/dash/${model}/`);
    setActiveNavItem(model);
}

function loadModelDetail(model, id = null) {
    const url = id ? `/dash/${model}/${id}/` : `/dash/${model}/create/`;
    loadContent(url);
}

function submitForm(model, id = null) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const url = id ? `/dash/${model}/${id}/` : `/dash/${model}/create/`;

    fetch(url, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            loadModelList(model);
        } else {
            alert('Error al enviar el formulario.');
        }
    })
    .catch(error => console.error('Error en la petición:', error));
}

document.addEventListener('DOMContentLoaded', function() {
    const scrollBtn = document.getElementById('scrollTopBtn');
    if (scrollBtn) {
        scrollBtn.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Set initial active state and load content if necessary
    const path = window.location.pathname;
    if (path === '/dashboard/' || path === '/dash/') {
        setActiveNavItem();
        loadContent('/dash//');  // Assuming you have a home view
    } else if (path.includes('/dash/')) {
        const model = path.split('/')[2];
        setActiveNavItem(model);
        loadModelList(model);
    }
});

function setActiveNavItem(model) {
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });
    
    if (!model || model === 'home') {
        document.querySelector('a.nav-item[href*="dashboard"]').classList.add('active');
    } else {
        const element = document.querySelector(`button.nav-item[onclick*="${model}"]`);
        if (element) {
            element.classList.add('active');
        }
    }
}

function loadContent(url) {
    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.getElementById('content').innerHTML = html;
        })
        .catch(error => console.error('Error loading content:', error));
}

function loadModelList(model) {
    loadContent(`/dash/${model}/`);
    setActiveNavItem(model);
}

function loadModelDetail(model, id = null) {
    const url = id ? `/dash/${model}/${id}/` : `/dash/${model}/create/`;
    loadContent(url);
}

function submitForm(model, id = null) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const url = id ? `/dash/${model}/${id}/` : `/dash/${model}/create/`;

    fetch(url, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            loadModelList(model);
        } else {
            alert('Error al enviar el formulario.');
        }
    })
    .catch(error => console.error('Error en la petición:', error));
}

// shrink header when scroll
const header = document.querySelector('header');
window.addEventListener('scroll', () => {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        header.classList.add('shrink');
    } else {
        header.classList.remove('shrink');
    }
})
