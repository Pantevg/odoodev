openerp.mass_editing = function(instance, local) {

    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;

  //  instance.web.ViewManager =  instance.web.Widget.extend({
function firstWord(s) {
  var word = s[0]+s[1]+s[2]+s[3];
  return word;
}
function modalClass(){
  if ($("#body").hasClass("modal-open")) {
    $(".modal-dialog").attr("id", "modalStyled");

    setTimeout(function(){$("#modalStyled").append('<div><script id="asivakk">$("#modalStyled span.oe_form_field.oe_form_field_radio.oe_vertical > span > div").click(function() {$(this).find("label").attr("for", "");$("div", $(this).parent()).each(function() {$(this).removeClass("activeButtonAS").find("input").prop("checked", false);});$(this).addClass("activeButtonAS").find("input").prop("checked", true);});</script></div>');$("#modalStyled .oe_form_field_many2many_list_row_add").attr("colspan", "3");}, 100);
  }else{
    setTimeout(modalClass, 100);
  }
}

      instance.web.View.include({
          load_view: function () {
              return $.when(this._super().done(function(){
          //      console.log("1");
                if ($("#asivak")[0]) {}else{
                  variableA = 0;
                  $.each( $('.oe_sidebar'), function(i, oe_sidebar) {
                //    console.log("2");
                     $('div', oe_sidebar).each(function() {
                      //    console.log("3");
                          var button = $(this).find("button").text().trim();
                          if (button == "More" || button == "Action") {
                            var dropDown = $(this).find(".oe_dropdown_menu");
                            $.each( $(this).find(".oe_dropdown_menu"), function(i, oe_dropDown) {
                          //    console.log("4");
                               $('li', oe_dropDown).each(function() {
                            //     console.log("5");
                                var mass = firstWord($(this).text().trim());
                                if (mass == "Mass") {
                                  if (variableA == 0) {
                                      $(".oe_sidebar").append('<div id="asivak" class="oe_form_dropdown_section"><button class="oe_dropdown_toggle oe_dropdown_arrow">Edit<i class="fa fa-caret-down" style="margin-left: 4px;"></i></button><ul class="oe_dropdown_menu"></ul></div>');
                                  }else{}
                                  variableA++;
                                  var wordHere = $(this).find("a").html().split("(");
                                  var wordFinished = wordHere[1].split(")");
                                  $(this).find("a").html(wordFinished[0]);
                                  $("#asivak ul").append('<li class="oe_sidebar_action modalMassEdit">'+ $(this).html() +'</li>');
                                  $(this).attr("style", "display: none;");
                                  $(".modalMassEdit").click(function() {modalClass()});

                                }
                               });
                            });
                          }
                     });
                  });
                }
              }));
          }
      });

      /*/ Vitalik Demchenko /*/
      instance.web.Sidebar.include({
        init: function(parent){
          var res = this._super.apply(this, arguments);
          _.each(this.sections, function(section){
            if(section.label == 'More'){
              section.label = _t('Action');
            }
          });
          return res;
        },
      });
      /*/ Vitalik Demchenko /*/
}
