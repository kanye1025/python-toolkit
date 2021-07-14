# -*- coding: utf-8 -*-

import os


class mf_model:
    def __init__(self,tr,va = None,fun= None,k=None,nr_threads= None,nr_bins= None,fold = None,nr_iters = None,l1=None,l2 = None,r= None,do_mnf= None):
        '''
        :param tr:  [(u,v,r)] or filepath（str）
        :param va:  [(u,v,r)] or filepath（str）
        :param fun: "set loss function (default 0)\n"
                    " for real-valued matrix factorization\n"
                    "\t 0 -- squared error (L2-norm)\n"
                    "\t 1 -- absolute error (L1-norm)\n"
                    "\t 2 -- generalizedKL-divergence\n"
                    "  for binary matrix factorization\n"
                    "\t 5 -- logarithmic loss\n"
                    "\t 6 -- squared hinge loss\n"
                    "\t 7 -- hinge loss\n"
                    "  for one-class matrix factorization\n"
                    "\t10 -- row-oriented pairwise logarithmic loss\n"
                    "\t11 -- column-oriented pairwise logarithmic loss\n"
        :param k:
        :param nr_threads:
        :param nr_bins:    set number of bins (may be adjusted by LIBMF)
        :param nr_iters:
        :param l1:  float or  (float,float) set L1-regularization parameters for P and Q (default 0)  P and Q share the same lambda if only one lambda is specified
        :param l2:  float or  (float,float) set L2-regularization parameters for P and Q (default 0.1)  P and Q share the same lambda if only one lambda is specified
        :param r: learning rate (default 0.1)
        :param do_mnf: perform non-negative matrix factorization
        :param fold: set number of folds for cross validation\n"
        '''

        self._P = []
        self._Q = []
        '''
        self.params = {}
        self.params['fun'] = fun
        self.params['k'] = k
        self.params['nr_threads'] = nr_threads
        self.params['nr_bins'] = nr_bins
        self.params['nr_iters'] = nr_iters
        self.params['r'] = r
        self.params['do_mnf'] = do_mnf
        '''
        if type(tr) != str:
            with open('tr_tmp','w') as f:
                for pt in tr:
                    f.write(str(pt[0])+' '+str(pt[1])+' '+str(pt[2])+'\n')
            tr = 'tr_tmp'
            if va:
                with open('va_tmp', 'w') as f:
                    for pt in va:
                        f.write(str(pt[0]) + ' ' + str(pt[1]) + ' ' + str(pt[2])+'\n')
                va = 'tr_tmp'

        param_str = ''
        if fun:
            param_str +=' -f '+str(fun)
        if l1:
            if type(l1) == list and len(l1) == 2:
                param_str +=' -l1 '+str(l1[0]) + ' , '+str(l1[1])
            else:
                param_str += ' -l1 ' + str(l1)
        if l2:
            if type(l2) == list and len(l2) == 2:
                param_str +=' -l2 '+str(l2[0]) + ' , '+str(l2[1])
            else:
                param_str += ' -l2 ' + str(l2)
        if k:
            param_str +=' -k '+str(k)
        if nr_iters:
            param_str +=' -t '+str(nr_iters)
        if nr_threads:
            param_str += ' -s ' + str(nr_threads)
        if nr_bins:
            param_str += ' -n ' + str(nr_bins)
        if r:
            param_str += ' -r ' + str(r)
        if va:
            param_str += ' -p %s '%(va)
        if do_mnf:
            param_str += '  --nmf '
        if fold:
            param_str += ' -v  %d  '%(fold)


        print(os.getcwd())
        print(param_str,tr)
        print('./bin/mf-train  %s  %s  mf_model_tmp'%(param_str,tr))
        os.system('./bin/mf-train  %s  %s  mf_model_tmp'%(param_str,tr))
        #os.remove('tr_tmp')
        #if  va:
           #os.remove('va_tmp')

        with open('./mf_model_tmp','r') as f:
            next(f)
            self.m = int(next(f)[2:-1])
            self.n = int(next(f)[2:-1])
            next(f)
            next(f)
            for line in f:
                if line[0] == 'p':
                    p = []
                    if 'T' in line:
                        for s in line[1:-2].split('T')[1].split(' ')[1:]:
                            p.append(float(s))
                    elif 'F' in line:
                        for s in line[1:-2].split('F')[1].split(' ')[1:]:
                            p.append(float(s))
                    else:
                        assert(False)
                    self._P.append(p)
                elif line[0] == 'q':
                    q = []
                    if 'T' in line:
                        for s in line[1:-2].split('T')[1].split(' ')[1:]:
                            q.append(float(s))
                    elif 'F' in line:
                        for s in line[1:-2].split('F')[1].split(' ')[1:]:
                            q.append(float(s))
                    else:
                        assert(False)
                    self._Q.append(q)
        #os.remove('mf_model_tmp')

    def predict(self,va,fun = 0):
        '''
        :param va:  暂时只支持验证集文件地址
        :param fun:
                "\t 0 -- root mean square error\n"
                "\t 1 -- mean absolute error\n"
                "\t 2 -- generalized KL-divergence\n"
                "\t 5 -- logarithmic error\n"
                "\t 6 -- accuracy\n"
                "\t10 -- row-wise mean percentile rank\n"
                "\t11 -- column-wise mean percentile rank\n"
                "\t12 -- row-wise area under the curve\n"
                "\t13 -- column-wise area under the curve\n");
        :return:
            float-list

        '''
        ret = []
        os.system('./bin/mf-predict  -e %d  %s    ./mf_model_tmp   ./mf_pre_tmp'%(fun, va))
        with open('mf_pre_tmp','r') as f:
            for line in f:
                ret.append(float(line.strip()))
        return ret
    def P(self):
        return self._P

    def Q(self):
        return self._Q

    def M(self):
        return self.m

    def N(self):
        return self.n

