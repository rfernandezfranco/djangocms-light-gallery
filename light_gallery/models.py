from django.db import models
import django
if django.VERSION[0] < 4:
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.translation import gettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from filer.fields.folder import FilerFolderField
from filer.models.imagemodels import Image
import uuid

MODES = [
    ['lg-slide', 'lg-slide'], ['lg-fade', 'lg-fade'], ['lg-zoom-in', 'lg-zoom-in'],
    ['lg-zoom-in-big', 'lg-zoom-in-big'], ['lg-zoom-out', 'lg-zoom-out'],
    ['lg-zoom-out-big', 'lg-zoom-out-big'], ['lg-zoom-out-in', 'lg-zoom-out-in'],
    ['lg-zoom-in-out', 'lg-zoom-in-out'], ['lg-soft-zoom', 'lg-soft-zoom'],
    ['lg-scale-up', 'lg-scale-up'], ['lg-slide-circular', 'lg-slide-circular'],
    ['lg-slide-circular-vertical', 'lg-slide-circular-vertical'],
    ['lg-slide-vertical', 'lg-slide-vertical'],
    ['lg-slide-vertical-growth', 'lg-slide-vertical-growth'],
    ['lg-slide-skew-only', 'lg-slide-skew-only'],
    ['lg-slide-skew-only-rev', 'lg-slide-skew-only-rev'],
    ['lg-slide-skew-only-y', 'lg-slide-skew-only-y'],
    ['lg-slide-skew-only-y-rev', 'lg-slide-skew-only-y-rev'],
    ['lg-slide-skew', 'lg-slide-skew'], ['lg-slide-skew-rev', 'lg-slide-skew-rev'],
    ['lg-slide-skew-cross', 'lg-slide-skew-cross'],
    ['lg-slide-skew-cross-rev', 'lg-slide-skew-cross-rev'],
    ['lg-slide-skew-ver', 'lg-slide-skew-ver'],
    ['lg-slide-skew-ver-rev', 'lg-slide-skew-ver-rev'],
    ['lg-slide-skew-ver-cross', 'lg-slide-skew-ver-cross'],
    ['lg-slide-skew-ver-cross-rev', 'lg-slide-skew-ver-cross-rev'],
    ['lg-lollipop', 'lg-lollipop'], ['lg-lollipop-rev', 'lg-lollipop-rev'],
    ['lg-rotate', 'lg-rotate'], ['lg-rotate-rev', 'lg-rotate-rev'],
    ['lg-tube', 'lg-tube']
]
ALIGN_THUMBNAILS_CHOICES = [['left', 'Left'], ['middle', 'Middle'], ['right', 'Right']]

class LightGallery(CMSPlugin):
    folder = FilerFolderField(
        verbose_name=_('Folder'),
        on_delete=models.CASCADE,
    )
    pageThumbWidth = models.CharField(_("Page Thumb Width"), max_length=255, default="150", help_text=_("Width of thumbnail on page"))
    pageThumbHeight = models.CharField(_("Page Thumb Height"), max_length=255, default="150", help_text=_("Height of thumbnail on page"))
    pageThumbMarginHorizontal = models.CharField(_("Page Thumb Horizontal Margin"), max_length=255, default="0px", help_text=_("Horizontal margin of thumbnail on page"))
    pageThumbMarginVertical = models.CharField(_("Page Thumb Vertical Margin"), max_length=255, default="5px", help_text=_("Vertical margin of thumbnail on page"))

    mode = models.CharField(_("Mode"), choices=MODES, default=MODES[0], help_text=_("Type of transition between images"), max_length=255)
    cssEasing = models.CharField(_("CSS Easing"), max_length=255, default="ease", help_text=_("Slide animation CSS easing property."))
    speed = models.PositiveIntegerField(_("Speed"), default=400, help_text=_("Transition duration (in ms)"))
    height = models.CharField(_("Height"), max_length=255, default="100%", help_text=_("Height of the gallery"))
    width = models.CharField(_("Width"), max_length=255, default="100%", help_text=_("Width of the gallery"))
    addClass = models.CharField(_("Add Class"), max_length=255, default="", help_text=_("Add custom class for gallery, can be used to set different style for different gallery"), blank=True)
    startClass = models.CharField(_("Start Class"), max_length=255, default="lg-start-zoom", help_text=_("Starting animation class for the gallery"))
    backdropDuration = models.PositiveIntegerField(_("Backdrop Duration"), default=300, help_text=_("Lightgallery backdrop transtion duration. Do not change the value of backdrop via css"))
    hideBarsDelay = models.PositiveIntegerField(_("Hide Bars Delay"), default=0, help_text=_("Delay for hiding gallery controls in ms. Pass 0 if you don't want to hide the controls."))
    closable = models.BooleanField(_("Closable"), default=True, help_text=_("Allows clicks on dimmer to close gallery"))
    loop = models.BooleanField(_("Loop"), default=True, help_text=_("If false, will disable the ability to loop back to the beginning of the gallery when on the last element"))
    escKey = models.BooleanField(_("ESC Key"), default=True, help_text=_("Whether the LightGallery could be closed by pressing the 'Esc' key"))
    keyPress = models.BooleanField(_("Key Press"), default=True, help_text=_("Enable keyboard navigation"))
    controls = models.BooleanField(_("Controls"), default=True, help_text=_("If false, prev/next buttons will not be displayed"))
    slideEndAnimation = models.BooleanField(_("Slide End Animation"), default=True, help_text=_("Enable slideEnd animation"))
    hideControlOnEnd = models.BooleanField(_("Hide Control On End"), default=False, help_text=_("If true, prev/next button will be hidden on first/last image"))
    mousewheel = models.BooleanField(_("Mousewheel"), default=False, help_text=_("Change slide on mousewheel"))
    preload = models.PositiveIntegerField(_("Preload"), default=2, help_text=_("Number of preload slides. will execute only after the current slide is fully loaded"))
    nextHtml = models.CharField(_("Next Html"), max_length=255, default="", help_text=_("Custom html for next control"), blank=True)
    prevHtml = models.CharField(_("Prev Html"), max_length=255, default="", help_text=_("Custom html for prev control"), blank=True)
    index = models.PositiveIntegerField(_("Index"), default=0, help_text=_("Allows to set which image/video should load initially"))
    download = models.BooleanField(_("Download"), default=True, help_text=_("Enable download button"))
    counter = models.BooleanField(_("Counter"), default=True, help_text=_("Whether to show total number of images and index number of currently displayed image"))
    appendCounterTo = models.CharField(_("Append Counter To"), max_length=255, default=".lg-toolbar", help_text=_("Where the counter should be appended"))
    swipeThreshold = models.PositiveIntegerField(_("Swipe Threshold (core)"), default=50, help_text=_("By setting the swipeThreshold (in px) you can set how far the user must swipe for the next/prev image"))
    enableDrag = models.BooleanField(_("Enable Drag"), default=True, help_text=_("Enables desktop mouse drag support"))
    enableSwipe = models.BooleanField(_("Enable Swipe"), default=True, help_text=_("Enables swipe support"))

    # New fields from v2.8.3
    allowMediaOverlap = models.BooleanField(_("Allow Media Overlap"), default=False)
    appendSubHtmlTo = models.CharField(_("Append SubHTML To"), max_length=50, default='.lg-sub-html')
    closeOnTap = models.BooleanField(_("Close On Tap"), default=True, help_text="Allows clicks on black area to close gallery.")
    defaultCaptionHeight = models.PositiveIntegerField(_("Default Caption Height"), default=0)
    getCaptionFromTitleOrAlt = models.BooleanField(_("Get Caption From Title Or Alt"), default=True)
    hideScrollbar = models.BooleanField(_("Hide Scrollbar"), default=False)
    iframeHeight = models.CharField(_("IFrame Height"), max_length=20, default='100%')
    iframeMaxWidth = models.CharField(_("IFrame Max Width"), max_length=255, default="100%", help_text=_("Set maximum width for iframe."))
    iframeMaxHeight = models.CharField(_("IFrame Max Height"), max_length=20, default='100%')
    iframeWidth = models.CharField(_("IFrame Width"), max_length=20, default='100%')
    licenseKey = models.CharField(_("License Key"), max_length=30, default='0000-0000-000-0000', blank=True)
    loadYouTubePoster = models.BooleanField(_("Load YouTube Poster"), default=True)
    mobileControls = models.BooleanField(_("Mobile Controls"), default=False, help_text="Enable controls on mobile devices.")
    mobileShowCloseIcon = models.BooleanField(_("Mobile Show Close Icon"), default=False, help_text="Show close icon on mobile devices.")
    mobileDownload = models.BooleanField(_("Mobile Download"), default=False, help_text="Enable download button on mobile devices.")
    numberOfSlideItemsInDom = models.PositiveIntegerField(_("Number of Slide Items In DOM"), default=10, help_text="Control how many slide items should be kept in dom at a time (min 3).")
    resetScrollPosition = models.BooleanField(_("Reset Scroll Position"), default=True)
    showBarsAfter = models.PositiveIntegerField(_("Show Bars After"), default=10000, help_text="Delay in hiding controls for the first time when gallery is opened.")
    showCloseIcon = models.BooleanField(_("Show Close Icon"), default=True)
    showMaximizeIcon = models.BooleanField(_("Show Maximize Icon"), default=False)
    slideDelay = models.PositiveIntegerField(_("Slide Delay"), default=0)
    startAnimationDuration = models.PositiveIntegerField(_("Start Animation Duration"), default=400)
    subHtmlSelectorRelative = models.BooleanField(_("SubHTML Selector Relative"), default=False)
    swipeToClose = models.BooleanField(_("Swipe To Close"), default=True)
    trapFocus = models.BooleanField(_("Trap Focus"), default=True)
    videoMaxSize = models.CharField(_("Video Max Size"), max_length=20, default='1280-720')
    zoomFromOrigin = models.BooleanField(_("Zoom From Origin"), default=True)

    # Thumbnail settings
    thumbnail = models.BooleanField(_("Enable Thumbnails"), default=True, help_text=_("Enable thumbnails for the gallery."))
    animateThumb = models.BooleanField(_("Enable Thumbnail Animation"), default=True)
    alignThumbnails = models.CharField(_("Align Thumbnails"), choices=ALIGN_THUMBNAILS_CHOICES, max_length=255, default=ALIGN_THUMBNAILS_CHOICES[1][0], help_text=_("Position of thumbnails when the width of all thumbnails combined is less than the gallery's width."))
    thumbWidth = models.PositiveIntegerField(_("Thumb Width"), default=100, help_text=_("Width of each thumbnails"))
    thumbHeight = models.CharField(_("Thumb Height"), max_length=20, default='80px', help_text=_("Height of each thumbnails."))
    thumbMargin = models.PositiveIntegerField(_("Thumb Margin"), default=5, help_text=_("Spacing between each thumbnails"))
    showThumbByDefault = models.BooleanField(_("Show/Hide thumbnails by default"), default=True)
    toggleThumb = models.BooleanField(_("Toggle Thumbnail Button"), default=False, help_text=_("Enable toggle captions and thumbnails button."))
    enableThumbDrag = models.BooleanField(_("Enable Thumbnail Drag"), default=True, help_text=_("Enables desktop mouse drag support for thumbnails"))
    enableThumbSwipe = models.BooleanField(_("Enable Thumbnail Swipe"), default=True, help_text=_("Enables thumbnail touch/swipe support for touch devices"))
    thumbnailSwipeThreshold = models.PositiveIntegerField(_("Thumbnail Swipe Threshold"), default=10, help_text=_("Swipe threshold for thumbnails."))
    appendThumbnailsTo = models.CharField(_("Append Thumbnails To"), max_length=50, default='.lg-components', help_text="Control where the thumbnails should be appended.")
    loadYouTubeThumbnail = models.BooleanField(_("Load YouTube Thumbnail (Thumbnail Plugin)"), default=True, help_text="Automatically load thumbnails for YouTube videos (thumbnail plugin).")
    youTubeThumbSize = models.PositiveIntegerField(_("YouTube Thumbnail Size (Thumbnail Plugin)"), default=1, help_text="YouTube thumbnail size (thumbnail plugin).")

    # Zoom settings
    zoom = models.BooleanField(_("Enable Zoom Buttons"), default=True) # Default changed as per general expectation for zoom plugin
    zoomScale = models.FloatField(_("Scale"), default=1, help_text=_("Value of zoom should be incremented/decremented")) # Changed to FloatField for scale
    zoomEnableZoomAfter = models.PositiveIntegerField(_("Enable Zoom After"), default=300, help_text=_("Number in ms"))
    actualSize = models.BooleanField(_("Enable Actual Size Button"), default=True, help_text="Enable actual size icon.")
    infiniteZoom = models.BooleanField(_("Infinite Zoom"), default=True, help_text="Enable/Disable infinite zoom for zoom plugin.")
    showZoomInOutIcons = models.BooleanField(_("Show Zoom In/Out Icons"), default=False, help_text="Show zoom in, zoom out icons for zoom plugin.")

    # Fullscreen settings
    fullscreen = models.BooleanField(_("Enable Fullscreen Button"), default=True) # Default changed as per general expectation

    # Pager settings
    pager = models.BooleanField(_("Enable Pager"), default=True, help_text=_("Enable/disable pager for this gallery")) # Default changed

    # Hash settings
    hash = models.BooleanField(_("Enable Hash"), default=True, help_text=_("Enable/Disable hash plugin")) # Default changed
    galleryId = models.CharField(_("Gallery Id"), max_length=255, default="1", help_text=("Unique id for each gallery. It is mandatory when you use hash plugin for multiple galleries on the same page")) # Changed to CharField for flexibility

    # Share settings
    share = models.BooleanField(_("Enable/Disable share plugin"), default=True)
    facebook = models.BooleanField(_("Enable Facebook share"), default=True)
    facebookDropdownText = models.CharField(_("Facebook dropdown text"), default="Facebook", max_length=255)
    twitter = models.BooleanField(_("Enable Twitter share"), default=True)
    twitterDropdownText = models.CharField(_("Twitter dropdown text"), default="Twitter", max_length=255)
    pinterest = models.BooleanField(_("Enable Pinterest share"), default=True)
    pinterestDropdownText = models.CharField(_("Pinterest dropdown text"), default="Pinterest", max_length=255)

    # Autoplay plugin settings
    autoplay = models.BooleanField(_("Autoplay"), default=True, help_text="Enable autoplay plugin.")
    autoplayControls = models.BooleanField(_("Autoplay Controls"), default=True, help_text="Show/hide autoplay controls.")
    appendAutoplayControlsTo = models.CharField(_("Append Autoplay Controls To"), max_length=50, default='.lg-toolbar', help_text="Specify where the autoplay controls should be appended.")
    forceSlideShowAutoplay = models.BooleanField(_("Force SlideShow Autoplay"), default=False, help_text="If false autoplay will be stopped after first user action.")
    progressBar = models.BooleanField(_("Progress Bar"), default=True, help_text="Show autoplay progress bar.")
    slideShowAutoplay = models.BooleanField(_("SlideShow Autoplay"), default=False, help_text="Enable slideshow autoplay.")
    slideShowInterval = models.PositiveIntegerField(_("SlideShow Interval"), default=5000, help_text="Time (in ms) between each auto transition for slideshow.")

    # Rotate plugin settings
    rotate = models.BooleanField(_("Rotate"), default=True, help_text="Enable/Disable rotate plugin.")
    rotateLeft = models.BooleanField(_("Rotate Left Button"), default=True, help_text="Enable rotate left button.")
    rotateRight = models.BooleanField(_("Rotate Right Button"), default=True, help_text="Enable rotate right button.")
    flipHorizontal = models.BooleanField(_("Flip Horizontal Button"), default=True, help_text="Enable flip horizontal button.")
    flipVertical = models.BooleanField(_("Flip Vertical Button"), default=True, help_text="Enable flip vertical button.")
    rotateSpeed = models.PositiveIntegerField(_("Rotate Speed"), default=400, help_text="Rotate speed in milliseconds.")

    def get_folder_images(self):
        images = self.folder.files.instance_of(Image)
        return images.filter(is_public=True)

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]

    def parse_page_thumb_width_height(self):
        return "%sx%s" % (self.pageThumbWidth, self.pageThumbHeight)
