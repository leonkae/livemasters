console.log("i am a live! stunnning!!")
document.addEventListener("DOMContentLoaded", () => {
    const mainProgressBar = document.querySelector(
      ".progress-bar--primary .progress-bar__fill"
    );
    const mainPosts = document.querySelectorAll(".main-post");
    const posts = document.querySelectorAll(".post");
  
    let progress = 0;
    let postIndex = 0;
    let interval;
  
    function startProgress() {
      interval = setInterval(() => {
        if (progress >= 100) {
          progress = 0;
          nextPost();
        } else {
          progress += 1;
          updateProgressBar();
        }
      }, 100);
    }
  
    function updateProgressBar() {
      mainProgressBar.style.width = `${progress}%`;
      posts[postIndex].querySelector(".progress-bar__fill").style.width = `${progress}%`;
    }
  
    function resetProgressBar() {
      mainProgressBar.style.width = "0%";
      posts.forEach((post) => post.querySelector(".progress-bar__fill").style.width = "0%");
    }
  
    function nextPost() {
      clearInterval(interval);
      resetProgressBar();
  
      posts[postIndex].classList.remove("post--active");
      mainPosts[postIndex].classList.remove("main-post--active");
      mainPosts[postIndex].classList.add("main-post--not-active");
  
      postIndex = (postIndex + 1) % posts.length;
  
      posts[postIndex].classList.add("post--active");
      mainPosts[postIndex].classList.add("main-post--active");
      mainPosts[postIndex].classList.remove("main-post--not-active");
  
      progress = 0;
      startProgress();
    }
  
    posts.forEach((post, index) => {
      post.addEventListener("click", () => {
        clearInterval(interval);
        postIndex = index;
        progress = 0;
        resetProgressBar();
        updateActivePosts();
        startProgress();
      });
    });
  
    function updateActivePosts() {
      posts.forEach((post) => post.classList.remove("post--active"));
      mainPosts.forEach((mainPost) => {
        mainPost.classList.remove("main-post--active");
        mainPost.classList.add("main-post--not-active");
      });
  
      posts[postIndex].classList.add("post--active");
      mainPosts[postIndex].classList.add("main-post--active");
      mainPosts[postIndex].classList.remove("main-post--not-active");
    }
  
    startProgress();
  });
  