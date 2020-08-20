const scroller = document.querySelector('#scroller');
const sentinel = document.querySelector('#sentinel');
const topbutton = document.querySelector('#totop');
let images = [];
let alldata = [];
let counter = 1;


// (Lazy Loading) Load image data from Flask View
function loadItems() {
  fetch(`/load?page=${counter}`).then((response) => {
    response.json().then((data) => {
      console.log(data);

      if (!data.length) {
        sentinel.innerHTML = "NO MORE IMAGES";
        return;
      }

      for (let i = 0; i < data.length; i++) {
        images.push(document.createElement('img'));
        data[i].DOM = images[images.length - 1];
        alldata.push(data[i]);
        images[images.length - 1].src = data[i]['url'];
        images[images.length - 1].className = 'image-item';
        scroller.appendChild(images[images.length - 1]);
      }

      alldata.forEach(item => {
        $(item.DOM).on('click', function (e) {
          lightbox.classList.add('active');
          const flink = document.createElement('a');
          const focus = document.createElement('img');
          flink.className = 'focus';
          focus.className = 'focus';
          flink.href = item['unsplashed'];
          focus.src = this.src;

          const desc = document.createElement('label');
          if(item['caption'] == null)
            desc.innerHTML = "Image by " + item['author'];
          else {
            if(item['caption'].length > 50)
              desc.innerHTML = item['caption'].substring(0, 50) + '...';
            else
              desc.innerHTML = item['caption'];
          }
          desc.id = 'caption';
          while(lightbox.firstChild)
            lightbox.removeChild(lightbox.firstChild);

          lightbox.appendChild(flink);
          flink.appendChild(focus);
          lightbox.appendChild(desc);
        })
      })
    })
  })
}

// (Lazy Loading) Intersection Observer
const intersectionObserver = new IntersectionObserver(entries => {
  if (entries.some(entry => entry.intersectionRatio > 0)) {
    setTimeout(function () {
      loadItems();
      counter += 1;
    }, 200);
  }
});
intersectionObserver.observe(sentinel);


// (Top Scroll) Block top scroll button
window.onscroll = () => {
  if (document.documentElement.scrollTop > 300)
    topbutton.style.display = "block";
  else {
    topbutton.setAttribute('animation', 'animation: scale-out-hor-left 0.5s cubic-bezier(0.550, 0.085, 0.680, 0.530) both;')
    topbutton.style.display = "none";
  }
}

// (Top Scroll) Scroller
topbutton.onclick = () => {
  window.scrollTo({top: 0, behavior: "smooth"})
}


// Image Lightbox
const lightbox = document.createElement('div');
lightbox.id = 'lightbox';
document.body.appendChild(lightbox);

lightbox.addEventListener('click', e => {
  if(e.target !== e.currentTarget)
      return;
  lightbox.classList.remove('active');
})

