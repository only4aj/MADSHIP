const input = () =>{
    let n = document.getElementById('name').value
    let te = document.getElementById('tel').value
    
    localStorage.setItem(n,te)
    let w = document.getElementById('work').innerText =localStorage.getItem(n.value);
    let test = document.getElementById('test')
    w.innerText = localStorage.getItem(n.value)
    test.innerText = localStorage.getItem(n)
}

// function setData(){
//     let set = document.getElementById('content').textContent
//     // let set = document.getElementById('content').innerHTML
//     document.getElementById('test1').innerText = set
//     // test.innerHTML = String(set)
//     // test.innerHTML = (set)
//     console.log(set)
//     console.log(typeof(set))
// }

// window.onload = function(){
//         let set = document.getElementById('content').textContent
//         // let set = document.getElementById('content').innerHTML
//         document.getElementById('test1').innerText = set
//         // test.innerHTML = String(set)
//         // test.innerHTML = (set)
//         console.log(set)
//         console.log(typeof(set))
//     alert("Hello")
// }