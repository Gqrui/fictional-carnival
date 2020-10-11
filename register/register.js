// pages/register/register.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
  stuNum:"",
  password:"" //后端绑定前端
  },
  stunumInput:function(e){
    this.setData({stuNum:e.detail.value}); //前端绑定后端
  },
  passwordInput:function(e){
    this.setData({password:e.detail.value}); 
  },
  login:function(){
     console.log(this.data.stuNum, this.data.password);//获取数据，将验证码发送给后端，后端进行校验等操作
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})