import * as echarts from 'echarts';
import DOMPurify from 'dompurify';
import { marked } from 'marked';

// Expose these as globals so the existing inline scripts in echarts.html
// can access them exactly as they would if they were loaded via CDN.
window.echarts = echarts;
window.DOMPurify = DOMPurify;
window.marked = marked;
