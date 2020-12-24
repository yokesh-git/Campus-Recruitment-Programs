#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
    int N,ind,total=0,possible_sum_arr_ind,temp,p,ans,p1,p2,sum=0,ka;
    scanf("%d",&N);
    int vehicle[N];
    for(ind=1;ind<=N;ind++)
    {
        scanf("%d",&vehicle[ind]);
        total = total + vehicle[ind];
    }

    int possible_sum_arr[total];

    for(ind=1;ind<=N;ind++)
    {
        p = vehicle[ind];
        possible_sum_arr[p] = 1;
    }

    for(ind=1;ind<=N;ind++)
    {
        temp = total - vehicle[ind];
        possible_sum_arr[temp] = 1;
    }
    if(total%2 == 1)
    {
        float m;
        m = ceil((total/2.0));
        //printf("%f",m);
        ka = m;
        if(ka%2==1) m = ceil((total/2.0));
        else m = ceil((total/2.0))+1;
        ka = m;
        //printf("\nM is %d",ka);
    }
    else
    {
        ka = total/2;
    }

    possible_sum_arr[ka] = 1;
    possible_sum_arr[total] = 1;
    for(possible_sum_arr_ind=1;possible_sum_arr_ind<=total;possible_sum_arr_ind++)
    {
        if(possible_sum_arr[possible_sum_arr_ind] != 1)
        {
            possible_sum_arr[possible_sum_arr_ind] = 0;
        }
    }
    /*printf("\n");
    for(possible_sum_arr_ind=1;possible_sum_arr_ind<=total;possible_sum_arr_ind++)
    {
        printf("%d ",possible_sum_arr[possible_sum_arr_ind]);
    }*/

    for(possible_sum_arr_ind=1;possible_sum_arr_ind<=ka;possible_sum_arr_ind++)
    {
        ans = total - possible_sum_arr_ind;
        if(possible_sum_arr[ans] == 1)
        {
                p1 = ans;
                p2 = possible_sum_arr_ind;
                //printf("\n%d %d\n",p1,p2);
        }
    }
    if(p1>=p2)
    {
        printf("%d ",p1);
    }
    else
    {
        printf("%d ",p2);
    }


    return 0;
}
