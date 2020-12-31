const  makeIsFreeTier = (id, model) => {
    $.ajax({
        type: "POST",
        url: "{% url 'toggle_freetier' %}",
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