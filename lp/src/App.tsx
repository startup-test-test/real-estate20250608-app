import React, { useState, useEffect } from 'react';
import { 
  Building2, 
  Zap, 
  BarChart3, 
  Users, 
  Shield, 
  ArrowRight, 
  Check, 
  Star,
  Menu,
  X,
  Phone,
  Mail,
  MapPin,
  Search,
  TrendingUp,
  Brain,
  Globe,
  Lock,
  Cpu,
  Home,
  Calculator,
  FileText,
  Settings,
  ChevronRight,
  Target,
  Database,
  PieChart,
  Folder,
  AlertCircle,
  DollarSign,
  TrendingDown,
  Clock,
  CheckCircle2,
  Sparkles,
  Zap as ZapIcon,
  LogIn
} from 'lucide-react';

function App() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [scrollY, setScrollY] = useState(0);

  useEffect(() => {
    const handleScroll = () => setScrollY(window.scrollY);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const toggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <div className="min-h-screen bg-white">
      {/* Navigation */}
      <nav className="bg-slate-700 shadow-sm sticky top-0 z-50 border-b border-slate-600">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-3">
              <div className="w-8 h-8 bg-white rounded-lg flex items-center justify-center">
                <Home className="h-5 w-5 text-slate-700" />
              </div>
              <span className="text-xl font-bold text-white">大家DX</span>
            </div>
            
            {/* Desktop Navigation */}
            <div className="hidden md:flex items-center space-x-8">
              <a href="#features" className="text-gray-300 hover:text-white transition-colors font-medium">3つのAI機能</a>
              <a href="#demo" className="text-gray-300 hover:text-white transition-colors font-medium">デモ</a>
              <a href="#pricing" className="text-gray-300 hover:text-white transition-colors font-medium">料金</a>
              <a href="#contact" className="text-gray-300 hover:text-white transition-colors font-medium">お問合わせ</a>
              <button className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-2.5 rounded-full hover:shadow-lg hover:scale-105 transition-all duration-200 font-medium">
                無料ではじめる
              </button>
              <a href="#login" className="flex items-center border-2 border-gray-300 text-gray-300 hover:text-white hover:border-white transition-all duration-200 px-4 py-2 rounded-full font-medium">
                <LogIn className="h-4 w-4 mr-2" />
                ログイン
              </a>
            </div>

            {/* Mobile menu button */}
            <div className="md:hidden">
              <button
                onClick={toggleMobileMenu}
                className="text-gray-300 hover:text-white"
              >
                {mobileMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
              </button>
            </div>
          </div>

          {/* Mobile Navigation */}
          {mobileMenuOpen && (
            <div className="md:hidden py-4 border-t border-slate-600 bg-slate-700">
              <div className="flex flex-col space-y-4">
                <a href="#features" className="text-gray-300 hover:text-white transition-colors font-medium">機能</a>
                <a href="#demo" className="text-gray-300 hover:text-white transition-colors font-medium">デモ</a>
                <a href="#pricing" className="text-gray-300 hover:text-white transition-colors font-medium">料金</a>
                <a href="#contact" className="text-gray-300 hover:text-white transition-colors font-medium">お問い合わせ</a>
                <button className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-2.5 rounded-full hover:shadow-lg transition-all duration-200 font-medium w-fit">
                  かんたん60秒！無料ではじめる
                </button>
                <a href="#login" className="flex items-center border-2 border-gray-300 text-gray-300 hover:text-white hover:border-white transition-all duration-200 px-4 py-2 rounded-full font-medium w-fit">
                  <LogIn className="h-4 w-4 mr-2" />
                  ログイン
                </a>
              </div>
            </div>
          )}
        </div>
      </nav>

      {/* Hero Section - ファーストビュー */}
      <section className="relative bg-gradient-to-br from-gray-50 via-white to-blue-50 overflow-hidden">
        {/* Background Elements */}
        <div className="absolute inset-0 bg-grid-pattern opacity-5"></div>
        <div className="absolute top-20 right-20 w-72 h-72 bg-gradient-to-br from-blue-400/20 to-purple-400/20 rounded-full blur-3xl"></div>
        <div className="absolute bottom-20 left-20 w-96 h-96 bg-gradient-to-br from-purple-400/20 to-pink-400/20 rounded-full blur-3xl"></div>
        
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 lg:py-32">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            {/* Left Content */}
            <div className="text-center lg:text-left">
              <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold leading-tight mb-8">
                <span className="bg-gradient-to-r from-blue-600 via-purple-600 to-blue-800 bg-clip-text text-transparent text-3xl sm:text-4xl lg:text-6xl">565万件の<br />ビッグデータ×AIで、</span>
                <br />
                <span className="bg-gradient-to-r from-gray-900 via-gray-800 to-gray-900 bg-clip-text text-transparent">賃貸経営を支援</span>
              </h1>
              
              <p className="text-xl text-gray-600 max-w-4xl mx-auto lg:mx-0 mb-12 leading-relaxed">
                収支予測から地価・人口動向まで、すべての判断材料を一元化。データドリブンな投資判断で、賃貸経営の成功確率を高めます。
              </p>
              
              <div className="flex flex-col sm:flex-row gap-6 justify-center lg:justify-start items-center mb-16">
                <button className="group bg-gradient-to-r from-blue-600 to-purple-600 text-white px-10 py-4 rounded-full hover:shadow-2xl hover:scale-105 transition-all duration-300 font-semibold text-lg relative overflow-hidden">
                  <span className="relative z-10 flex items-center">
                    かんたん60秒！無料ではじめる
                    <ArrowRight className="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform" />
                  </span>
                  <div className="absolute inset-0 bg-gradient-to-r from-purple-600 to-blue-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                </button>
              </div>
              
              <div className="flex items-center justify-center lg:justify-start space-x-8 text-sm text-gray-500">
               
              </div>
            </div>

            {/* Right Content - Dashboard Image */}
            <div className="relative">
              <div className="bg-white rounded-2xl shadow-2xl overflow-hidden border border-gray-200">
                <img 
                  src="/メインビジュアルの右画像 copy.png" 
                  alt="大家DXのダッシュボード画面"
                  className="w-full h-auto"
                />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Problems Section - 解決できる課題 */}
      <section className="py-24 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-20">
            <h2 className="text-4xl lg:text-5xl font-bold mb-6">
              <span className="bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">不動産を購入の際に<br></br>こんなお悩みありませんか？</span>
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              多くの大家さんが抱える、投資判断の不安を解決します
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              {
                number: "①",
                title: "相場が分からない",
                features: ["適正賃料は？売却価格は？", "長期的な投資判断ができない"]
              },
              {
                number: "②",
                title: "収支が不安",
                features: ["本当に利益は出る？", "修繕費や空室リスクは大丈夫？"]
              },
              {
                number: "③",
                title: "情報収集が大変",
                features: ["類似物件の取引事例が見つからない", "信頼できるデータがない"]
              }
            ].map((item, index) => (
              <div key={index} className="group bg-white p-8 rounded-3xl border border-gray-100 hover:border-gray-200 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
                <div className="flex items-center mb-6">
                  <span className="text-3xl font-bold text-blue-600 mr-4">{item.number}</span>
                  <h3 className="text-xl font-semibold text-gray-900">{item.title}</h3>
                </div>
                <ul className="space-y-3">
                  {item.features.map((feature, featureIndex) => (
                    <li key={featureIndex} className="flex items-start">
                      <span className="text-gray-400 mr-3 mt-1">•</span>
                      <span className="text-gray-600 leading-relaxed">{feature}</span>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Service Overview - サービス概要 */}
      <section id="features" className="py-24 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-20">
            <h2 className="text-4xl lg:text-5xl font-bold mb-6">
              <span className="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">大家DXの3つのAI機能</span>
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              {
                icon: Target,
                title: "投資シミュレーション",
                description: "物件価格・家賃・融資条件から自動で30年収支を計算。キャッシュフロー、IRR、NPVまで詳細分析。",
                gradient: "from-blue-100 to-blue-200",
                iconColor: "blue",
                features: ["30年間の詳細収支計算", "修繕費・空室率を考慮", "複数シナリオ比較"]
              },
              {
                icon: BarChart3,
                title: "市場分析AI",
                description: "エリアの価格推移・人口動態・賃料相場・リスクを予測。将来性を数値化して投資判断をサポート。",
                gradient: "from-blue-100 to-blue-200",
                iconColor: "blue",
                features: ["人口・世帯数の将来予測", "地価・賃料の推移分析", "リスクスコア算出"]
              },
              {
                icon: Search,
                title: "取引事例検索",
                description: "類似物件の成約価格・利回り・構造をワンクリックで取得。565万件超のデータベースから最適な比較対象を発見。",
                gradient: "from-blue-100 to-blue-200",
                iconColor: "blue",
                features: ["565万件超の取引データ", "類似条件での自動検索", "適正価格の算出"]
              }
            ].map((service, index) => (
              <div key={index} className={`group bg-gradient-to-br ${service.gradient} p-8 rounded-3xl hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 relative overflow-hidden border border-blue-200`}>
                <div className="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -translate-y-16 translate-x-16"></div>
                <div className="relative z-10">
                  <div className="flex items-center space-x-4 mb-6">
                    <div className={`bg-blue-600 w-12 h-12 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform duration-300`}>
                      <service.icon className="h-6 w-6 text-white" />
                    </div>
                    <h3 className="text-2xl font-bold text-gray-900">{service.title}</h3>
                  </div>
                  <p className="text-gray-700 mb-8 text-lg leading-relaxed">
                    {service.description}
                  </p>
                  <ul className="space-y-4">
                    {service.features.map((feature, featureIndex) => (
                      <li key={featureIndex} className="flex items-center">
                        <CheckCircle2 className="h-5 w-5 text-blue-600 mr-3 flex-shrink-0" />
                        <span className="text-gray-700">{feature}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Demo Section - スクリーンショット */}
      <section id="demo" className="py-24 bg-gradient-to-br from-gray-50 to-blue-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-20">
            <h2 className="text-4xl lg:text-5xl font-bold mb-6">
              <span className="bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">操作はかんたん。</span>
              <span className="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">結果は本格的。</span>
            </h2>
            <p className="text-xl text-gray-600">
              直感的なUIで、プロレベルの分析結果を即座に取得
            </p>
          </div>
          
          {/* Mock Dashboard */}
          <div className="bg-white rounded-3xl shadow-2xl overflow-hidden border border-gray-100 backdrop-blur-sm">
            {/* Dashboard Header */}
            <div className="bg-gradient-to-r from-gray-800 to-gray-900 px-8 py-6 flex items-center justify-between">
              <div className="flex items-center space-x-4">
                <div className="w-8 h-8 bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
                  <Home className="h-5 w-5 text-white" />
                </div>
                <span className="text-white font-semibold text-lg">大家DX</span>
              </div>
              <div className="text-gray-300 text-sm bg-gray-700/50 px-4 py-2 rounded-full">東後 吉郎 さん</div>
            </div>
            
            {/* Dashboard Content */}
            <div className="flex">
              {/* Sidebar */}
              <div className="w-72 bg-gradient-to-b from-gray-800 to-gray-900 min-h-96">
                <nav className="p-6 space-y-3">
                  {[
                    { icon: Home, label: "マイページ", active: true },
                    { icon: Calculator, label: "AI物件シミュレーター", active: false },
                    { icon: Search, label: "AI取引事例検索", active: false },
                    { icon: BarChart3, label: "AI市場分析", active: false }
                  ].map((item, index) => (
                    <div key={index} className={`flex items-center space-x-3 px-4 py-3 rounded-xl cursor-pointer transition-all duration-200 ${
                      item.active 
                        ? 'bg-gradient-to-r from-blue-600 to-purple-600 text-white shadow-lg' 
                        : 'text-gray-300 hover:bg-gray-700/50 hover:text-white'
                    }`}>
                      <item.icon className="h-5 w-5" />
                      <span className="font-medium">{item.label}</span>
                    </div>
                  ))}
                </nav>
              </div>
              
              {/* Main Content */}
              <div className="flex-1 p-8 bg-gradient-to-br from-gray-50 to-white">
                <div className="mb-10">
                  <h3 className="text-3xl font-bold text-gray-900 mb-3">投資の成果を一目で確認</h3>
                  <p className="text-gray-600 text-lg">データで差をつける投資判断をサポートします</p>
                </div>
                
                {/* Feature Cards */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
                  {[
                    {
                      icon: Calculator,
                      title: "AI物件シミュレーター",
                      description: "物件の収益性と価格妥当性を、AIがまとめて分析します。",
                      gradient: "from-blue-600 to-purple-600"
                    },
                    {
                      icon: Search,
                      title: "AI取引事例検索",
                      description: "565万件超の取引データから類似物件の事例を検索・分析します。",
                      gradient: "from-green-500 to-teal-600"
                    },
                    {
                      icon: BarChart3,
                      title: "AI市場分析",
                      description: "エリアの市場動向と将来性をAIが詳細に分析します。",
                      gradient: "from-purple-600 to-pink-600"
                    }
                  ].map((card, index) => (
                    <div key={index} className={`bg-gradient-to-br ${card.gradient} text-white p-6 rounded-2xl hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1`}>
                      <div className="flex items-center space-x-3 mb-4">
                        <div className="bg-white/20 backdrop-blur-sm w-10 h-10 rounded-xl flex items-center justify-center">
                          <card.icon className="h-5 w-5" />
                        </div>
                        <span className="font-semibold">{card.title}</span>
                      </div>
                      <p className="text-white/90 text-sm mb-4 leading-relaxed">{card.description}</p>
                      <button className="bg-white/20 backdrop-blur-sm text-white px-4 py-2 rounded-xl text-sm hover:bg-white/30 transition-all duration-200 flex items-center group">
                        {card.title.includes('シミュレーター') ? '物件をAI分析する' : 
                         card.title.includes('検索') ? '取引事例を検索する' : '市場分析を表示する'}
                        <ChevronRight className="h-4 w-4 ml-1 group-hover:translate-x-1 transition-transform" />
                      </button>
                    </div>
                  ))}
                </div>
                
                {/* Property List Preview */}
                <div className="bg-white rounded-2xl p-8 shadow-lg border border-gray-100">
                  <div className="flex items-center justify-between mb-8">
                    <h4 className="text-xl font-semibold text-gray-900 flex items-center">
                      <FileText className="h-6 w-6 mr-3 text-purple-600" />
                      登録済み物件一覧
                    </h4>
                    <div className="flex space-x-3">
                      <button className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-3 rounded-xl text-sm hover:shadow-lg transition-all duration-200 transform hover:scale-105">
                        + 新規シミュレーション
                      </button>
                      <button className="border border-gray-200 text-gray-600 px-6 py-3 rounded-xl text-sm hover:bg-gray-50 transition-colors">
                        エクスポート
                      </button>
                    </div>
                  </div>
                  
                  <div className="text-gray-600 text-sm mb-6">8件の物件が見つかりました。</div>
                  
                  {/* Sample Property Cards */}
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                    {[
                      {
                        type: "一棟アパートマンション",
                        name: "天沼町",
                        location: "埼玉県さいたま市大宮区天沼町",
                        price: "0.7万円",
                        income: "384万円",
                        surfaceYield: "55014.33%",
                        realYield: "52.8%",
                        gradient: "from-blue-100 to-blue-200",
                        typeColor: "blue"
                      },
                      {
                        type: "区分マンション",
                        name: "クレメント川越",
                        location: "埼玉県川越市南所沢",
                        price: "1000.0万円",
                        income: "84万円",
                        surfaceYield: "8.4%",
                        realYield: "5.4%",
                        gradient: "from-orange-100 to-orange-200",
                        typeColor: "orange"
                      },
                      {
                        type: "一棟アパート",
                        name: "新宿区アパート",
                        location: "東京都新宿区",
                        price: "8500.0万円",
                        income: "520万円",
                        surfaceYield: "6.1%",
                        realYield: "5.8%",
                        gradient: "from-gray-100 to-gray-200",
                        typeColor: "gray"
                      }
                    ].map((property, index) => (
                      <div key={index} className="border border-gray-200 rounded-2xl overflow-hidden hover:shadow-lg transition-all duration-300 transform hover:-translate-y-1 group">
                        <div className={`h-32 bg-gradient-to-br ${property.gradient} relative`}>
                          <span className={`absolute top-3 left-3 bg-${property.typeColor}-600 text-white px-3 py-1 rounded-full text-xs font-medium`}>
                            {property.type}
                          </span>
                          <span className="absolute top-3 right-3 bg-green-600 text-white px-3 py-1 rounded-full text-xs font-medium">
                            収益
                          </span>
                        </div>
                        <div className="p-6">
                          <h5 className="font-semibold text-gray-900 mb-1 text-lg">{property.name}</h5>
                          <p className="text-sm text-gray-600 mb-4">{property.location}</p>
                          <div className="grid grid-cols-2 gap-4 text-sm mb-4">
                            <div>
                              <div className="text-gray-500 mb-1">取得価格</div>
                              <div className="font-semibold text-gray-900">{property.price}</div>
                            </div>
                            <div>
                              <div className="text-gray-500 mb-1">年間収入</div>
                              <div className="font-semibold text-gray-900">{property.income}</div>
                            </div>
                          </div>
                          <div className="grid grid-cols-2 gap-4 text-sm">
                            <div>
                              <div className="text-gray-500 mb-1">表面利回り</div>
                              <div className="font-semibold text-green-600">{property.surfaceYield}</div>
                            </div>
                            <div>
                              <div className="text-gray-500 mb-1">実質利回り</div>
                              <div className="font-semibold text-blue-600">{property.realYield}</div>
                            </div>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials - ユーザーの声 */}
      <section className="py-24 bg-gradient-to-br from-gray-50 to-blue-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-20">
            <h2 className="text-4xl lg:text-5xl font-bold mb-6">
              <span className="bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">使ってわかる、投資判断の</span>
              <span className="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">「納得感」。</span>
            </h2>
            <p className="text-xl text-gray-600">
              実際にご利用いただいているお客様からの評価
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {[
              {
                name: "田中 太郎様",
                role: "埼玉県・30代大家さん",
                avatar: "田中",
                color: "blue",
                testimonial: "購入前にキャッシュフローを精密に試算できたので、安心してローンを組めました。特にAI市場分析で将来の賃料推移まで予測できるのが素晴らしいです。"
              },
              {
                name: "佐藤 花子様",
                role: "東京都・40代投資家",
                avatar: "佐藤",
                color: "green",
                testimonial: "迷っていた2物件を比較して、回収力と出口価格で優劣を見極められました。取引事例検索で類似物件の成約価格も確認でき、適正価格での購入ができました。"
              }
            ].map((testimonial, index) => (
              <div key={index} className="group bg-white p-10 rounded-3xl border border-gray-100 shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2">
                <div className="flex items-center mb-6">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} className="h-5 w-5 text-yellow-400 fill-current" />
                  ))}
                </div>
                <p className="text-gray-700 mb-8 leading-relaxed text-lg font-medium">
                  「{testimonial.testimonial}」
                </p>
                <div className="flex items-center">
                  <div className={`w-14 h-14 bg-gradient-to-br from-${testimonial.color}-100 to-${testimonial.color}-200 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform duration-300`}>
                    <span className={`text-${testimonial.color}-700 font-bold text-lg`}>{testimonial.avatar}</span>
                  </div>
                  <div className="ml-4">
                    <h4 className="font-semibold text-gray-900 text-lg">{testimonial.name}</h4>
                    <p className="text-sm text-gray-500">{testimonial.role}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section id="pricing" className="py-24 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-20">
            <h2 className="text-4xl lg:text-5xl font-bold mb-6">
              <span className="bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">まずは無料で</span>
              <span className="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">はじめてみませんか？</span>
            </h2>
            <p className="text-xl text-gray-600">
              すべてのプランで30日間無料トライアル
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">
            <div className="bg-white p-10 rounded-3xl border border-gray-200 shadow-lg hover:shadow-xl transition-all duration-300">
              <h3 className="text-2xl font-semibold text-gray-900 mb-3">フリープラン</h3>
              <p className="text-gray-600 mb-8">まずはお試しで</p>
              <div className="mb-8">
                <span className="text-5xl font-bold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">無料</span>
              </div>
              <ul className="space-y-4 mb-10">
                {["物件3件まで登録", "収支計算機能", "基本的な市場分析"].map((feature, index) => (
                  <li key={index} className="flex items-center">
                    <Check className="h-5 w-5 text-green-600 mr-4 flex-shrink-0" />
                    <span className="text-gray-700">{feature}</span>
                  </li>
                ))}
              </ul>
              <button className="w-full bg-gray-100 text-gray-700 py-4 rounded-2xl hover:bg-gray-200 transition-colors font-semibold text-lg">
                無料でAI分析をはじめる
              </button>
            </div>

            <div className="bg-gradient-to-br from-blue-600 to-purple-600 text-white p-10 rounded-3xl relative transform scale-105 shadow-2xl">
              <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
                <span className="bg-gradient-to-r from-yellow-400 to-orange-400 text-gray-900 px-6 py-2 rounded-full text-sm font-bold shadow-lg">
                  おすすめ
                </span>
              </div>
              <h3 className="text-2xl font-semibold mb-3">プレミアムプラン</h3>
              <p className="text-blue-100 mb-8">本格的な投資分析に</p>
              <div className="mb-8">
                <span className="text-5xl font-bold">¥1,980</span>
                <span className="text-blue-100 text-xl">/月〜</span>
              </div>
              <ul className="space-y-4 mb-10">
                {["保存件数無制限", "全AI機能利用可能", "CSVエクスポート", "共有機能"].map((feature, index) => (
                  <li key={index} className="flex items-center">
                    <Check className="h-5 w-5 text-white mr-4 flex-shrink-0" />
                    <span className="text-blue-100">{feature}</span>
                  </li>
                ))}
              </ul>
              <button className="w-full bg-white text-blue-600 py-4 rounded-2xl hover:bg-gray-50 transition-colors font-semibold text-lg shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-200">
                30日間無料トライアル
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-24 bg-gradient-to-br from-gray-900 via-blue-900 to-purple-900 relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-blue-600/20 to-purple-600/20"></div>
        <div className="absolute top-0 left-0 w-full h-full bg-grid-pattern opacity-10"></div>
        
        <div className="relative max-w-4xl mx-auto text-center px-4 sm:px-6 lg:px-8">
          <h2 className="text-4xl lg:text-5xl font-bold text-white mb-8 leading-tight">
            あなたの投資判断を、<br />
            <span className="bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">もっと科学的に。</span>
          </h2>
          <p className="text-xl text-gray-300 mb-12 leading-relaxed">
            データで差をつける不動産投資を、今すぐ始めませんか？
          </p>
          <div className="flex flex-col sm:flex-row gap-6 justify-center mb-8">
            <button className="group bg-gradient-to-r from-blue-600 to-purple-600 text-white px-10 py-4 rounded-full hover:shadow-2xl hover:scale-105 transition-all duration-300 font-semibold text-lg relative overflow-hidden">
              <span className="relative z-10 flex items-center justify-center">
                今すぐ無料でAI分析をはじめる
                <ArrowRight className="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform" />
              </span>
              <div className="absolute inset-0 bg-gradient-to-r from-purple-600 to-blue-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            </button>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer id="contact" className="bg-gray-900 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-12">
            <div className="col-span-1 md:col-span-2">
              <div className="flex items-center space-x-3 mb-6">
                <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl flex items-center justify-center">
                  <Home className="h-6 w-6 text-white" />
                </div>
                <span className="text-2xl font-bold bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">大家DX</span>
              </div>
              <p className="text-gray-400 mb-8 max-w-md leading-relaxed">
                データで差をつける不動産投資。AIと最新テクノロジーで投資判断を科学的にサポートします。
              </p>
              <div className="space-y-4">
                {[
                  { icon: Phone, text: "03-1234-5678" },
                  { icon: Mail, text: "info@daikadx.com" },
                  { icon: MapPin, text: "東京都港区六本木1-1-1" }
                ].map((contact, index) => (
                  <div key={index} className="flex items-center space-x-4">
                    <div className="bg-gray-800 w-10 h-10 rounded-xl flex items-center justify-center">
                      <contact.icon className="h-5 w-5 text-blue-400" />
                    </div>
                    <span className="text-gray-300">{contact.text}</span>
                  </div>
                ))}
              </div>
            </div>
            
            <div>
              <h3 className="font-semibold mb-6 text-lg">サービス</h3>
              <ul className="space-y-3">
                {["機能一覧", "料金プラン", "導入事例", "API"].map((item, index) => (
                  <li key={index}>
                    <a href="#" className="text-gray-400 hover:text-white transition-colors">{item}</a>
                  </li>
                ))}
              </ul>
            </div>
            
            <div>
              <h3 className="font-semibold mb-6 text-lg">サポート</h3>
              <ul className="space-y-3">
                {["ヘルプセンター", "お問い合わせ", "利用規約", "プライバシーポリシー"].map((item, index) => (
                  <li key={index}>
                    <a href="#" className="text-gray-400 hover:text-white transition-colors">{item}</a>
                  </li>
                ))}
              </ul>
            </div>
          </div>
          
          <div className="border-t border-gray-800 mt-16 pt-8 text-center">
            <p className="text-gray-400">
              © 2024 大家DX. All rights reserved.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;