# Wildlife Detection Model Training Data

## Data Sources

### 1. Dedicated Machine Learning & Research Datasets

These are often the best places to start because the data is collected and structured specifically for research and model training.

**iNaturalist**
A joint initiative of the California Academy of Sciences and the National Geographic Society. It's a massive citizen-science project with millions of photos and videos.

- **Why it's great:** Observations are often "research grade," meaning the community has verified the species identification. The data is available with Creative Commons licenses, and they have an API for easier access.
- **Link:** [iNaturalist Datasets](https://www.inaturalist.org/pages/developers)

**Caltech Camera Traps (CCT)**
A very large and popular dataset for object detection in camera trap imagery. While primarily images, camera traps often record short video clips, and image sequences are highly relevant for video model training.

- **Why it's great:** It's specifically designed for machine learning, contains millions of images/videos from diverse locations, and includes bounding box annotations.
- **Link:** [Caltech Camera Traps (CCT) Dataset](http://www.vision.caltech.edu/Image_Datasets/CCT20/)

### 2. Video Platforms with Permissive Licenses

These platforms host a vast amount of content, but you need to filter carefully to find usable videos.

**YouTube (with Creative Commons filter)**
YouTube is an enormous resource if you use its search filters correctly.

- **Why it's great:** Unmatched variety and volume. You can find videos of rare species and behaviors that might not be in curated datasets.
- **How to use it:**
    1. Search for a species (e.g., "red-tailed hawk").
    2. Click the "Filters" button.
    3. Under "Features," select "Creative Commons." This will show videos that creators have marked as reusable. Always double-check the license for each video.
- **Pro-Tip:** You can use a command-line tool like `yt-dlp` to download these videos.

**Vimeo**
Similar to YouTube, Vimeo hosts high-quality video content, and many creators use Creative Commons licenses.

- **Why it's great:** The video quality on Vimeo is often higher than on YouTube. It has a dedicated Creative Commons section.
- **Link:** [Vimeo Creative Commons Collection](https://vimeo.com/creativecommons)

### 3. Free Stock Footage Websites

These sites offer professionally shot, high-quality video clips under very permissive licenses.

**Pexels**
Provides high-quality and completely free stock photos and videos.

- **Why it's great:** The Pexels license is very simple and allows for commercial use with no attribution required (though it's appreciated). The quality is excellent for model training.
- **Link:** [Pexels Wildlife Videos](https://www.pexels.com/search/videos/wildlife/)

**Pixabay**
Another large repository of free-to-use images and videos.

- **Why it's great:** Similar to Pexels, it has a simple, permissive license and a huge library of content.
- **Link:** [Pixabay Wildlife Videos](https://pixabay.com/videos/search/wildlife/)

### 4. Government & Archival Sources

These are fantastic sources for public domain content, especially for species native to a specific region.

**U.S. Fish and Wildlife Service (FWS) National Digital Library**
A collection of public domain photos, videos, and sound clips.

- **Why it's great:** Content is generally in the public domain (check each item). It's a reliable source for North American wildlife.
- **Link:** [FWS National Digital Library](https://digitalmedia.fws.gov/)

**The Internet Archive**
A non-profit library of millions of free books, movies, software, music, websites, and more.

- **Why it's great:** Contains vast historical and contemporary collections, including nature documentaries and raw footage. You need to carefully check the usage rights for each item, as they vary.
- **Link:** [The Internet Archive](https://archive.org/)

## Important Considerations for Your Project

### Verify Licenses

This is the most critical step. "Free" doesn't always mean free for any use. Look for Public Domain (CC0) or Creative Commons (CC BY, CC BY-SA) licenses. Avoid anything with a "Non-Commercial" (NC) clause if your project might have commercial applications.

### Data Quality and Bias

Be aware that your dataset may have biases. For example, you might find more videos of diurnal (daytime) animals than nocturnal ones, or more videos from North America than from Africa. This can bias your model's performance.

### Data Augmentation

You will likely need to augment your data. For video, this can include:

- Extracting frames and applying image augmentations (rotation, flipping, color jitter).
- Varying playback speed.
- Using temporal augmentations like frame dropping.

### Labeling

Even with videos of a specific species, you will still need to go through and label the data. This means either labeling each frame with bounding boxes or classifying entire clips, which can be time-consuming.
