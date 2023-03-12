document.getElementById("file_upload").addEventListener("change", function (event) {
    console.log("File upload event triggered");
    // using fetch to send the file to the server
    var formData = new FormData();
    formData.append("file", event.target.files[0]);
    fetch("/api/model", {
        method: "POST",
        body: formData
    }).then(function (response) {
        return response.json();
    }
    ).then(function (data) {
        console.log(data);
    }
    );
});

function submit(){ 
    document.submit.submit()
}