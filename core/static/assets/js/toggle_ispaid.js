const  makeIspaid = (id, model) => {
    $.ajax({
        type: "POST",
        url: "{% url 'toggle_ispaid' %}",
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