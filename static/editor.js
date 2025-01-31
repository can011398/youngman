var editor;
function initEditor() {
    editor = new SimpleMDE({ element: document.getElementById("myEditor") });
}

function setContent() {
    editor.value("##")
}

function getContent() {
    var value = editor.value();
    console.log(value);
    const formData = new FormData();
    formData.append('notes',value);
    fetch('/upload',{method:'POST',body:formaData})
    .then(response=>{response.json()})
    .then(data=>{console.log('上传成功',data)})
    .catch(error=>{
        console.error('错误',error);})
    
}

function disableEditor() {
    editor.togglePreview();
}