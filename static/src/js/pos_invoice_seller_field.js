openerp.invoice_seller_field = function(instance){
    var module = instance.point_of_sale;
    var QWeb = instance.web.qweb;
	var _t = instance.web._t;

    module.HeaderSellerWidget = module.PosBaseWidget.extend({
        className: 'header-seller',
        start: function() {
            var self = this;
            var model = new instance.web.Model("pos.config");
            model.call("get_sellers", {context: new instance.web.CompoundContext()}).then(function(result) {
                self.$el.append(QWeb.render('HeaderSellerField', {sellers: result}));
            });
        },
    });

    module.PosWidget.include({
        build_widgets: function(){
            this._super();
            this.headerseller = new module.HeaderSellerWidget(this,{});
            this.headerseller.insertAfter(this.$('.pos-logo'));
        },
    });
}
