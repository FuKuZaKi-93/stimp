(function($) {
  'use strict';
  $('#collapseOne, #collapseTwo, #collapseThree').on({
    // 折り畳み開く処理
    'show.bs.collapse': function() {
      $('a[href="#' + this.id + '"] span.glyphicon-collapse-down')
        .removeClass('glyphicon-collapse-down')
        .addClass('glyphicon-collapse-up');
    },
    // 折り畳み閉じる処理
    'hide.bs.collapse': function() {
      $('a[href="#' + this.id + '"] span.glyphicon-collapse-up')
        .removeClass('glyphicon-collapse-up')
        .addClass('glyphicon-collapse-down');
    }
  });
})(jQuery);
