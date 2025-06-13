from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
import django
if django.VERSION[0] < 4:
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.translation import gettext_lazy as _

from .models import LightGallery


class LightGallery(CMSPluginBase):
    model = LightGallery
    name = _("Light Gallery")
    render_template = "light_gallery.html"
    cache = True

    fieldsets = (
        (None, {
            'fields': [
                'folder',
                ('pageThumbWidth',
                 'pageThumbHeight',
                 'pageThumbMarginVertical',
                 'pageThumbMarginHorizontal',),
            ]
        }),
        (_('Toolbar Settings'), {
            'fields': [
                'actualSize',
                'fullscreen',
                'zoom',
                'showMaximizeIcon',
                'download',
                'showCloseIcon',
                'controls',
            ]
        }),
        (_('Gallery Thumbnails'), {
            'classes': ['collapse', ],
            'fields': [
                'thumbnail',
                'animateThumb',
                'alignThumbnails',
                'thumbWidth',
                'thumbHeight',
                'thumbMargin',
                'showThumbByDefault',
                'toggleThumb',
                'enableThumbDrag',
                'enableThumbSwipe',
                'thumbnailSwipeThreshold', # Renamed from swipeThreshold for clarity
                'appendThumbnailsTo',
                'loadYouTubeThumbnail', # Assuming model field is loadYouTubeThumbnail
                'youTubeThumbSize',
            ]
        }),
        (_('Social Networks Sharing'), {
            'classes': ['collapse', ],
            'fields': [
                'share',
                'facebook',
                'facebookDropdownText',
                'twitter',
                'twitterDropdownText',
                'pinterest',
                'pinterestDropdownText',
            ]
        }),
        (_('Core Settings'), { # Renamed from _('Core')
            'classes': ['collapse', ],
            'fields': [
                'mode',
                'cssEasing',
                'speed',
                'height',
                'width',
                'addClass',
                'startClass',
                'backdropDuration',
                'hideBarsDelay', # Moved from old position
                'closable',
                'loop',
                'escKey',
                'keyPress',
                'hideControlOnEnd',
                'mousewheel',
                'preload',
                'nextHtml',
                'prevHtml',
                'index',
                'iframeMaxWidth',
                'counter',
                'appendCounterTo',
                'swipeThreshold', # General swipe threshold
                'enableDrag',
                'enableSwipe',
                'allowMediaOverlap',
                'appendSubHtmlTo',
                'closeOnTap',
                'defaultCaptionHeight',
                'getCaptionFromTitleOrAlt',
                'hideScrollbar',
                'iframeHeight',
                'iframeMaxHeight',
                'iframeWidth',
                'licenseKey',
                'loadYouTubePoster', # Assuming model field is loadYouTubePoster
                'numberOfSlideItemsInDom',
                'resetScrollPosition',
                'showBarsAfter',
                'slideDelay',
                'startAnimationDuration',
                'subHtmlSelectorRelative',
                'swipeToClose',
                'trapFocus',
                'videoMaxSize',
                'zoomFromOrigin',
            ]
        }),
        (_('Zoom Settings'), { # Renamed from _('Zoom')
            'classes': ['collapse', ],
            'fields': [
                'zoomScale',
                'zoomEnableZoomAfter',
                'infiniteZoom',
                'showZoomInOutIcons',
            ]
        }),
        (_('Pager Settings'), { # Renamed from _('Pager')
            'classes': ['collapse', ],
            'fields': [
                'pager',
            ]
        }),
        (_('Hash Settings'), { # Renamed from _('Hash')
            'classes': ['collapse', ],
            'fields': [
                'hash',
                'galleryId',
            ]
        }),
        (_('Autoplay Settings'), {
            'classes': ['collapse', ],
            'fields': [
                'autoplay',
                'autoplayControls',
                'appendAutoplayControlsTo',
                'forceSlideShowAutoplay',
                'progressBar',
                'slideShowAutoplay',
                'slideShowInterval',
            ]
        }),
        (_('Rotate Settings'), {
            'classes': ['collapse', ],
            'fields': [
                'rotate',
                'rotateLeft',
                'rotateRight',
                'flipHorizontal',
                'flipVertical',
                'rotateSpeed',
            ]
        }),
        (_('Mobile Overrides'), {
            'classes': ['collapse', ],
            'fields': [
                'mobileControls',
                'mobileShowCloseIcon',
                'mobileDownload',
            ]
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({
            'images': instance.get_folder_images(),
            'pageThumbWidthHeight': instance.parse_page_thumb_width_height(),
            'pageThumbMarginHorizontal': instance.pageThumbMarginHorizontal,
            'pageThumbMarginVertical': instance.pageThumbMarginVertical,
            'mode': instance.mode,
            'cssEasing': instance.cssEasing,
            'speed': instance.speed,
            'height': instance.height,
            'width': instance.width,
            'addClass': instance.addClass,
            'startClass': instance.startClass,
            'backdropDuration': instance.backdropDuration,
            'hideBarsDelay': instance.hideBarsDelay,
            'closable': instance.closable,
            'loop': instance.loop,
            'escKey': instance.escKey,
            'keyPress': instance.keyPress, # Corrected from instance.escKey
            'controls': instance.controls,
            'slideEndAnimation': instance.slideEndAnimation,
            'hideControlOnEnd': instance.hideControlOnEnd,
            'mousewheel': instance.mousewheel,
            'preload': instance.preload,
            'nextHtml': instance.nextHtml,
            'prevHtml': instance.prevHtml, # Added missing prevHtml
            'index': instance.index,
            'iframeMaxWidth': instance.iframeMaxWidth,
            'download': instance.download,
            'counter': instance.counter,
            'appendCounterTo': instance.appendCounterTo,
            'swipeThreshold': instance.swipeThreshold, # General swipeThreshold
            'enableDrag': instance.enableDrag,
            'enableSwipe': instance.enableSwipe,
            'id': instance.generate_id(),

            # New Core fields
            'allowMediaOverlap': instance.allowMediaOverlap,
            'appendSubHtmlTo': instance.appendSubHtmlTo,
            'closeOnTap': instance.closeOnTap,
            'defaultCaptionHeight': instance.defaultCaptionHeight,
            'getCaptionFromTitleOrAlt': instance.getCaptionFromTitleOrAlt,
            'hideScrollbar': instance.hideScrollbar,
            'iframeHeight': instance.iframeHeight,
            'iframeMaxHeight': instance.iframeMaxHeight,
            'iframeWidth': instance.iframeWidth,
            'licenseKey': instance.licenseKey,
            'loadYouTubePoster': instance.loadYouTubePoster, # Core loadYouTubePoster
            'numberOfSlideItemsInDom': instance.numberOfSlideItemsInDom,
            'resetScrollPosition': instance.resetScrollPosition,
            'showBarsAfter': instance.showBarsAfter,
            'showCloseIcon': instance.showCloseIcon,
            'showMaximizeIcon': instance.showMaximizeIcon,
            'slideDelay': instance.slideDelay,
            'startAnimationDuration': instance.startAnimationDuration,
            'subHtmlSelectorRelative': instance.subHtmlSelectorRelative,
            'swipeToClose': instance.swipeToClose,
            'trapFocus': instance.trapFocus,
            'videoMaxSize': instance.videoMaxSize,
            'zoomFromOrigin': instance.zoomFromOrigin,

            # Thumbnails
            'thumbnail': instance.thumbnail, # Renamed from thumbnails
            'animateThumb': instance.animateThumb,
            'alignThumbnails': instance.alignThumbnails, # Renamed from currentPagerPosition
            'thumbWidth': instance.thumbWidth,
            'thumbHeight': instance.thumbHeight, # Renamed from thumbContHeight
            'thumbMargin': instance.thumbMargin,
            'showThumbByDefault': instance.showThumbByDefault,
            'toggleThumb': instance.toggleThumb,
            'enableThumbDrag': instance.enableThumbDrag,
            'enableThumbSwipe': instance.enableThumbSwipe,
            'thumbnailSwipeThreshold': instance.thumbnailSwipeThreshold, # New thumbnail specific
            'appendThumbnailsTo': instance.appendThumbnailsTo,
            'loadYouTubeThumbnail': instance.loadYouTubeThumbnail, # Thumbnail specific
            'youTubeThumbSize': instance.youTubeThumbSize,

            # Zoom
            'fullscreen': instance.fullscreen,
            'zoom': instance.zoom,
            'zoomScale': instance.zoomScale,
            'zoomEnableZoomAfter': instance.zoomEnableZoomAfter,
            'actualSize': instance.actualSize, # Renamed from zoomActualSize
            'infiniteZoom': instance.infiniteZoom,
            'showZoomInOutIcons': instance.showZoomInOutIcons,

            # Pager
            'pager': instance.pager,

            # Hash
            'hash': instance.hash,
            'galleryId': instance.galleryId,

            # Share
            'share': instance.share,
            'facebook': instance.facebook,
            'facebookDropdownText': instance.facebookDropdownText,
            'twitter': instance.twitter,
            'twitterDropdownText': instance.twitterDropdownText,
            'pinterest': instance.pinterest,
            'pinterestDropdownText': instance.pinterestDropdownText,

            # Autoplay
            'autoplay': instance.autoplay,
            'autoplayControls': instance.autoplayControls,
            'appendAutoplayControlsTo': instance.appendAutoplayControlsTo,
            'forceSlideShowAutoplay': instance.forceSlideShowAutoplay,
            'progressBar': instance.progressBar,
            'slideShowAutoplay': instance.slideShowAutoplay,
            'slideShowInterval': instance.slideShowInterval,

            # Rotate
            'rotate': instance.rotate,
            'rotateLeft': instance.rotateLeft,
            'rotateRight': instance.rotateRight,
            'flipHorizontal': instance.flipHorizontal,
            'flipVertical': instance.flipVertical,
            'rotateSpeed': instance.rotateSpeed,

            # Mobile Overrides
            'mobileControls': instance.mobileControls,
            'mobileShowCloseIcon': instance.mobileShowCloseIcon,
            'mobileDownload': instance.mobileDownload,
        })
        return context

plugin_pool.register_plugin(LightGallery)
