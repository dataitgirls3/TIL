# Hyper_parameter_ Tuning_2019-12-02

피쳐를 다 정해주고 모든 작업을 마친 후에 이 모델의 성능을 최적화하고 싶을 때 하는 작업 

결과값 차이는 +- 5 % 

    y = aX

a 는 머신이 학습해서 정해주는 값

`e.g.` Decision Tree 

criterion = 'entropy', 'gini'

순도 100 일 때까지 학습하면 overfitting

max_depth, max_leafnode 를 정해주는 것

# Hyperparameter Tuning 방법

1. Manual Search 수동으로 하나씩 바꿔주는것

2. Grid Search : 하이퍼파라미터 범위를 정해준다(범위는 Manual Search 로 정해준다)

    searching 횟수는 파라미터 하나 * 파라미터 하나 * cv(cross validation) 수

    `e.g.` max_depth 를 10 부터 20 까지 1 단위로 본다

    `e.g.` 결정할 파라미터가 많다면 pair 로 넣어준다

    👎 설정해준 값만 시도해본다

3. Random Search

    범위를 주면 Uniform distribution 으로 랜덤하게 시도

    n_iter 뽑는 횟수

    search 범위가 늘어나면 n_iter 도 똑같이 늘려준다

    어디가 최적점일지 예상가능하다면 Distribution을 Gaussian Distribution 등으로 바꾼다. 

    `e.g.` n_iter = 10 

    👍 다양한 숫자들을 시도하기 때문에 최적점이 나올 확률이 높다

    👍 최적점 근처로 서치 범위를 좁혀서 다시 시도할 수 있다

Machine Learning 에서 Learning rate 가 중요하다

Random Forest 에서 n_estimator : Decision Tree 의 갯수

(!)Random 한 성격의 Model 을 쓸 때는 무조건 Random_state 를 설정해서 복원가능하게 한다(!)

**n_estimator 는 클수록 좋으니까**

1. best parameter 찾아서
2. dict 로 저장해서
3. n_estimator 만 큰 숫자로 바꿔서 model 새로 만들고 fit 한다