const  makeActive = (id, model) => {
    $.ajax({
        type: "POST",
        url: "{% url 'toggle' %}",
        data: {
           id: id, 
           model: model,
           csrfmiddlewaretoken: '{{ csrf_token }}'  
        },
        success: (res) => {
           location.reload()
        },
    
    });
}