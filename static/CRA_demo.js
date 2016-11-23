console.log('demo.js btn', document.getElementById('start-btn'));
document.getElementById('start-btn').onclick = function() {
    ServerHelper.demo_mode = false;
};