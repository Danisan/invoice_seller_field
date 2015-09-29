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
            $('.header-seller').on('change', '.sellers_select', function(){
                self.pos.get('selectedOrder').set_seller(this.value);
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

    var ModuleOrderSuper = module.Order;
    module.Order = module.Order.extend({
        initialize: function(options){
            ModuleOrderSuper.prototype.initialize.apply(this, arguments);
            this.set({
                seller: '00',
            });
        },
        export_as_JSON: function () {
            var res = ModuleOrderSuper.prototype.export_as_JSON.apply(this, arguments);
            res.seller_id = this.get_seller();
            return res;
        },
        set_seller: function(seller){
            this.set('seller', seller);
        },
        get_seller: function(){
            return this.get('seller');
        },
    });

}
