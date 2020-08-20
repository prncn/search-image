const scroller = document.querySelector('#scroller');
const sentinel = document.querySelector('#sentinel');
const topbutton = document.querySelector('#totop');
let alldata = [];
let counter = 1;


// (Lazy Loading) Load image data from Flask View
function loadItems() {
  fetch(`/load?page=${counter}`).then((response) => {
    response.json().then((data) => {

      if (!data.length) {
        sentinel.innerHTML = "NO MORE IMAGES";
        return;
      }

      for (let i = 0; i < data.length; i++) {
        data[i].DOM = document.createElement('img');
        data[i].DOM.src = data[i]['url'];
        data[i].DOM.className = 'image-item';
        scroller.appendChild(data[i].DOM);
        alldata.push(data[i]);
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
      });


      const display = $('.display');
      let _cols = Number(display.css('column-count'))
      for(let _col = 0; _col < _cols; _col++) {
          for (let i = 0; i < alldata.length; i += _cols) {
              if (alldata[i + _col].DOM !== undefined)
                scroller.appendChild(alldata[i + _col].DOM);

          }
      }

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
    console.log(alldata);
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


// Init Lightbox
const lightbox = document.createElement('div');
lightbox.id = 'lightbox';
document.body.appendChild(lightbox);

lightbox.addEventListener('click', e => {
  if(e.target !== e.currentTarget)
      return;
  lightbox.classList.remove('active');
})

